import matplotlib.pyplot as plt
import sys

y = [-1.47519e-05,0.000513613,0.000915718,-0.000261194,0.00085157,0.000335886,0.00109111,0.00131774,0.000725811,0.00141938,0.00161523,0.00149467,0.00039146,0.00149101,0.00195108,0.00247241,0.00143037,0.00242444,0.00165155,0.00247997,0.0025706,0.00166391,0.000596962,0.00137447,0.00149233,0.000868107,0.00126571,0.00160208,0.00010755,0.00104439,0.000674225,0.0020653,0.000927741,0.000646683,0.00115192,0.0028398,0.00142225,0.00279497,0.00245962,0.00249707,0.00282017,0.00268409,0.00307384,0.00241553,0.00330952,0.00173698,0.00188259,0.00134654,0.00217279,0.0024418,0.00224376,0.00249676,0.00106722,0.00252587,0.00298624,0.00158674,0.00140807,0.00117701,0.00135021,0.00023573,-9.2984e-05,-0.00267235,-0.00720003,-0.011295,-0.0185063,-0.0279896,-0.0374741,-0.0507542,-0.0626287,-0.0735793,-0.0868405,-0.0916205,-0.110487,-0.129586,-0.141504,-0.158603,-0.167355,-0.202087,-0.216313,-0.229785,-0.255312,-0.271684,-0.285182,-0.295443,-0.312203,-0.326955,-0.339212,-0.353218,-0.366131,-0.380485,-0.384683,-0.39782,-0.408477,-0.421514,-0.427373,-0.429007,-0.425584,-0.425729,-0.42393,-0.422921,-0.421878,-0.421411,-0.420413,-0.414763,-0.412175,-0.40611,-0.401627,-0.393475,-0.384352,-0.382739,-0.372566,-0.361926,-0.352644,-0.341203,-0.329414,-0.315385,-0.306562,-0.291246,-0.279109,-0.259191,-0.24709,-0.234866,-0.216377,-0.202885,-0.195015,-0.168927,-0.164812,-0.148014,-0.143352,-0.130178,-0.119494,-0.106836,-0.105098,-0.098653,-0.0823273,-0.0823502,-0.0757238,-0.0648106,-0.06252,-0.0542702,-0.0504182,-0.0452845,-0.0392075,-0.0361849,-0.0296067,-0.0258452,-0.021639,-0.0178804,-0.0135069,-0.0109357,-0.010402,-0.00643405,-0.00474788,-0.00173772,-0.00166761,0.000121666,-0.00291654,0.00102716,0.00118747,0.00106215,0.000438328,0.00123903,0.001237,0.000180835,-0.00166352,-0.00203699,-0.00547874,-0.0071043,-0.00949503,-0.0146957,-0.0186426,-0.0253897,-0.0277553,-0.0351299,-0.0406041,-0.04711,-0.0498291,-0.0542989,-0.0619277,-0.0678088,-0.0637002,-0.0747881,-0.0816476,-0.0825287,-0.0827098,-0.0986769,-0.0929217,-0.107341,-0.112331,-0.120269,-0.120767,-0.133969,-0.135106,-0.14512,-0.147131,-0.158127,-0.167973,-0.170045,-0.190746,-0.186752,-0.199682,-0.19858,-0.209543,-0.226381,-0.231185,-0.236248,-0.241103,-0.241921,-0.257914,-0.253562,-0.265705,-0.280431,-0.287865,-0.294366,-0.300781,-0.313292,-0.319164,-0.32577,-0.332917,-0.342729,-0.350136,-0.355707,-0.362586,-0.368988,-0.374535,-0.378281,-0.381143,-0.384525,-0.386464,-0.384963,-0.384632,-0.379923,-0.37757,-0.37464,-0.369448,-0.363932,-0.358015,-0.352421,-0.345378,-0.340075,-0.331003,-0.326605,-0.317578,-0.31389,-0.307095,-0.298521,-0.29175,-0.2847,-0.277924,-0.27207,-0.263498,-0.245547,-0.252095,-0.233966,-0.233488,-0.227786,-0.223626,-0.207136,-0.207699,-0.196312,-0.191602,-0.187045,-0.18311,-0.172986,-0.169101,-0.160229,-0.158921,-0.146506,-0.141666,-0.140544,-0.132503,-0.130559,-0.121513,-0.120505,-0.112967,-0.107886,-0.0968049,-0.0972271,-0.0907334,-0.0804855,-0.0816208,-0.0715032,-0.076022,-0.0669949,-0.0607967,-0.0595201,-0.0537101,-0.0503874,-0.045367,-0.0424758,-0.0382013,-0.0349341,-0.029913,-0.0249515,-0.0219141,-0.018041,-0.0132372,-0.0101506]
x = [i for i in range(len(y))]

fig2 = plt.figure()
ax = fig2.add_subplot()

a33, = ax.plot(x, y, color='red')

ax.set_xlabel("Video Frame")
ax.set_ylabel("State (m)")
plt.title("Prismatic State Optimization")
plt.show()

import math
# revolute stuff
y = [ 0.000829173,0.00533708,0.00135105,0.000448876,0.00859621,0.00294601,0.00724853,0.00719465,0.00435784,0.00324923,-0.000361372,-0.00523003,-0.014201,-0.0301586,-0.0455545,-0.0613883,-0.0825319,-0.0948319,-0.116666,-0.13388,-0.154546,-0.170129,-0.190074,-0.211434,-0.231129,-0.251479,-0.275826,-0.295823,-0.315574,-0.337709,-0.353321,-0.37426,-0.3908,-0.409767,-0.426213,-0.440836,-0.466267,-0.48581,-0.50914,-0.533976,-0.561726,-0.589716,-0.619419,-0.647321,-0.68158,-0.71112,-0.740885,-0.769197,-0.797774,-0.821376,-0.85031,-0.874474,-0.896111,-0.915926,-0.933007,-0.954142,-0.967749,-0.983715,-1.00162,-1.015,-1.02729,-1.04839,-1.0609,-1.07565,-1.08828,-1.10247,-1.11613,-1.13143,-1.1462,-1.16208,-1.17948,-1.19192,-1.20864,-1.22557,-1.24154,-1.25505,-1.27082,-1.28597,-1.30063,-1.3159,-1.32899,-1.34235,-1.35854,-1.37005,-1.38253,-1.39696,-1.40599,-1.41989,-1.43058,-1.44538,-1.45452,-1.46771,-1.47704,-1.48869,-1.50001,-1.50635,-1.51169,-1.52312,-1.52817,-1.53658,-1.53972,-1.54977,-1.55785,-1.54609,-1.55716,-1.54911,-1.54579,-1.54593,-1.54285,-1.53255,-1.53004,-1.50853,-1.4983,-1.48051,-1.46769,-1.44781,-1.42975,-1.41311,-1.39388,-1.37448,-1.35509,-1.33779,-1.32072,-1.30502,-1.29128,-1.27434,-1.26031,-1.24629,-1.23169,-1.21864,-1.2027,-1.19066,-1.17722,-1.16478,-1.15065,-1.14009,-1.12846,-1.1153,-1.10463,-1.09318,-1.08187,-1.06878,-1.05776,-1.04583,-1.0372,-1.0219,-1.00805,-0.993778,-0.981486,-0.967094,-0.951186,-0.936313,-0.92063,-0.90675,-0.888134,-0.874667,-0.858293,-0.845283,-0.831548,-0.817061,-0.804746,-0.795932,-0.784496,-0.774063,-0.765536,-0.754873,-0.747263,-0.737245,-0.726378,-0.718198,-0.708878,-0.700228,-0.689456,-0.682475,-0.669329,-0.661414,-0.64836,-0.634811,-0.627247,-0.612273,-0.59876,-0.581071,-0.569123,-0.551165,-0.532392,-0.513142,-0.492323,-0.469225,-0.447592,-0.422767,-0.406303,-0.389112,-0.375296,-0.364634,-0.356076,-0.348088,-0.338195,-0.329197,-0.321769,-0.308144,-0.297819,-0.285946,-0.272273,-0.262719,-0.249603,-0.241874,-0.235061,-0.221157,-0.213577,-0.207674,-0.196958,-0.190091,-0.183176,-0.176177,-0.166838,-0.158251,-0.151833,-0.143613,-0.135485,-0.129675,-0.120897,-0.111195,-0.10774,-0.0989708,-0.0927001,-0.0877745,-0.0797485,-0.0732167,-0.0655002,-0.0605311,-0.0529463,-0.0467716,-0.0394035,-0.0323082,-0.0266161,-0.0172951,-0.0084532,-0.00758361,0.0020891,0.00427061,0.00902754,0.0104381,0.0103465,0.0081526,0.0116969,0.00614993,0.00985579,0.00755333,0.00667808,0.00688267,0.00625442,0.00597472,0.00983923,0.0108446,0.00906201,0.0109055,0.00734638,0.00861646,0.00781335,0.0102923,0.00284586,0.00991713,0.00512767,0.0125582,0.00872173,0.00485479,0.00780455,0.00892198,0.01085,0.00673071,0.0100694,0.0098129,0.0100979,0.00896408,0.00430761,0.00929652,0.00775995,0.0077613,0.010712,0.00946724,0.00940098,0.013394,0.00970558,0.0127027,0.00660928,0.00766394,0.00939134,0.00521117,0.0117089,0.0122513,0.00925443,0.01217,0.0144144,0.00635264,0.00816825,0.011443,0.00895644,0.00881993,0.00705046]
y = [i / math.pi * 180 for i in y]
x = [i for i in range(len(y))]

figrev = plt.figure()

ax = figrev.add_subplot()
twin = ax.twinx()
a33, = ax.plot(x, y, color="green", label='33 p/frame')
ax.set_xlabel("Video Frame")
ax.set_ylabel("Theta (rad)")
plt.title("Revolute State Optimization")
plt.show()
# point cloud vis

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

file = open("/home/arnav/biswas/articulation/rev160.csv", "r")


def in_range(data, i):
    return (data[i][0] > 0.4 and data[i][0] < 0.9) and (
        data[i][1] > -0.19 and data[i][1] < 0.05) and (data[i][2] > 0
                                                      and data[i][2] < 0.6)


data = [[
    float(i.split(",")[0]),
    float(i.split(",")[1]),
    float(i.split(",")[2])
] for i in file.readlines()]

xs = [
    data[i][0] for i in range(len(data)) if i % 500 == 0 and in_range(data, i)
]

ys = [
    data[i][1] for i in range(len(data)) if i % 500 == 0 and in_range(data, i)
]

zs = [
    data[i][2] for i in range(len(data)) if i % 500 == 0 and in_range(data, i)
]

xsa = [
    data[i][0] for i in range(len(data))
    if i % 500 == 0 and not in_range(data, i)
]

ysa = [
    data[i][1] for i in range(len(data))
    if i % 500 == 0 and not in_range(data, i)
]

zsa = [
    data[i][2] for i in range(len(data))
    if i % 500 == 0 and not in_range(data, i)
]

print(len(xs))

ax.scatter(xs, ys, zs)
ax.scatter(xsa, ysa, zsa)
ax.scatter([0], [0], [0])
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
