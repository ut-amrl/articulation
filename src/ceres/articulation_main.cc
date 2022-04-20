#include <fstream>
#include <inttypes.h>
#include <math.h>
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>

#include "amrl_msgs/Localization2DMsg.h"
#include "config_reader/config_reader.h"
#include "eigen3/Eigen/Dense"
#include "eigen3/Eigen/Geometry"
#include "geometry_msgs/Pose2D.h"
#include "geometry_msgs/PoseArray.h"
#include "geometry_msgs/PoseStamped.h"
#include "geometry_msgs/PoseWithCovarianceStamped.h"
#include "gflags/gflags.h"
#include "glog/logging.h"
#include "nav_msgs/Odometry.h"
#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "sensor_msgs/PointCloud2.h"
#include "sensor_msgs/point_cloud2_iterator.h"
#include "shared/math/math_util.h"
#include "shared/ros/ros_helpers.h"
#include "shared/util/timer.h"
#include "visualization_msgs/Marker.h"
#include "visualization_msgs/MarkerArray.h"

#include "std_msgs/String.h"

#include "articulation.h"

using amrl_msgs::Localization2DMsg;
using articulation::Articulation;
using Eigen::Vector2f;
using Eigen::Vector3d;
using ros::Time;
using ros_helpers::Eigen2DToRosPoint;
using ros_helpers::Eigen3DToRosPoint;
using ros_helpers::RosPoint;
using ros_helpers::SetRosVector;
using std::string;
using std::vector;

CONFIG_DOUBLE(x_min_, "x_min");
CONFIG_DOUBLE(x_max_, "x_max");
CONFIG_DOUBLE(y_min_, "y_min");
CONFIG_DOUBLE(y_max_, "y_max");
CONFIG_DOUBLE(z_min_, "z_min");
CONFIG_DOUBLE(z_max_, "z_max");
CONFIG_UINT(num_points_, "num_points");
config_reader::ConfigReader config_reader_({"config/articulation.lua"});

int ddx = 0;
DEFINE_string(points_topic, "kinect_points", "Name of ROS Topic");
DEFINE_bool(vis, false, "debugging flag, to clean data");
DEFINE_string(type, "prismatic", "type of articulated joint");
DEFINE_bool(offline, false, "run optimization offline/online");
bool run_ = true;
Articulation *articulation_ = nullptr;

float ToFloat(uint8_t b0, uint8_t b1, uint8_t b2, uint8_t b3) {
  float f;
  uint8_t b[] = {b3, b2, b1, b0};
  memcpy(&f, &b, sizeof(f));
  return f;
}

void KinectCallback(const sensor_msgs::PointCloud2 &cloud_msg) {
  ddx += 1;
  if (FLAGS_vis && ddx != 125)
    return;

  std::vector<Vector3d> point_cloud;
  for (uint32_t i = 0; i < cloud_msg.height; i++) {
    for (uint32_t j = 0; j < cloud_msg.width * cloud_msg.point_step;
         j += cloud_msg.point_step) {
      size_t idx = i * cloud_msg.width * cloud_msg.point_step + j;
      double x = ToFloat(cloud_msg.data[idx + 3], cloud_msg.data[idx + 2],
                         cloud_msg.data[idx + 1], cloud_msg.data[idx + 0]);
      if (!FLAGS_vis && (!(x > CONFIG_x_min_ and x < CONFIG_x_max_) or x == 0))
        continue;
      double y = ToFloat(cloud_msg.data[idx + 7], cloud_msg.data[idx + 6],
                         cloud_msg.data[idx + 5], cloud_msg.data[idx + 4]);
      if (!FLAGS_vis && (!(y > CONFIG_y_min_ and y < CONFIG_y_max_) or y == 0))
        continue;
      double z = ToFloat(cloud_msg.data[idx + 11], cloud_msg.data[idx + 10],
                         cloud_msg.data[idx + 9], cloud_msg.data[idx + 8]);
      if (!FLAGS_vis && !(z > CONFIG_z_min_ and z < CONFIG_z_max_))
        continue;
      point_cloud.push_back({x, y, z});
    }
  }
  if (!FLAGS_vis)
    articulation_->UpdatePointCloud(point_cloud);

  if (FLAGS_vis) {
    std::string filename = "./rev125.csv";
    std::ofstream fout(filename);
    for (auto it : point_cloud) {
      if (!(it(0) == 0 && it(1) == 0)) {
        fout << it(0) << "," << it(1) << "," << it(2) << "," << std::endl;
      }
    }
    fout.close();
  }
}

void SignalHandler(int) {
  if (!run_) {
    printf("Force Exit.\n");
    exit(0);
  }
  printf("Exiting.\n");
  run_ = false;
}

int main(int argc, char **argv) {
  ddx = 0;
  google::ParseCommandLineFlags(&argc, &argv, false);
  signal(SIGINT, SignalHandler);
  // Initialize ROS.
  ros::init(argc, argv, "depth_factor", ros::init_options::NoSigintHandler);
  ros::NodeHandle n;
  articulation_ = new Articulation(&n, CONFIG_num_points_);

  ros::Subscriber kinect_sub =
      n.subscribe(FLAGS_points_topic, 1, &KinectCallback);

  RateLoop loop(20.0);
  while (run_ && ros::ok()) {
    ros::spinOnce();
    loop.Sleep();
  }

  if (!FLAGS_vis && FLAGS_offline) {
    if (FLAGS_type == "revolute") {
      articulation_->OptimizeRevoluteOffline();
    } else if (FLAGS_type == "prismatic") {
      articulation_->OptimizePrismaticOffline();
    }
  }

  delete articulation_;
  return 0;
}
