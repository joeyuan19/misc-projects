from math import floor, ceil, sqrt, pi
import matplotlib.pyplot as plt


def n_hex(n,m):
    return m*ceil(floor((2/sqrt(3))*n - 2/sqrt(3) + 1)/2) + (m - 1)*floor(floor((2/sqrt(3))*n - 2/sqrt(3) + 1)/2)

R = 1.
ratio = 0.75
r = R*ratio

m = 20
n = 100

v_round = (1./4)*(pi*pi)*(R + r)*((R - r)**2)
v_square = 4*(R-r)*(R*R - r*r)
print "ratio",v_square/v_round
print "ratio",v_round/v_square

N = 10

x = [i/float(N) for i in xrange(n*N)]


y = [v_square*m*floor(i) for i in x]
plt.plot(x,y,label="V_square",marker="",linestyle="-")

y = [v_round*m*floor(i) for i in x]
plt.plot(x,y,label="V_round_sq",marker="",linestyle="-")

y = [v_round*n_hex(i,m) for i in x]
plt.plot(x,y,label="V_round_hex",marker="",linestyle="-")

plt.title("Volume (V) per n by " + str(m)+" box")
plt.xlabel("n")
plt.ylabel("V")
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()
#plt.savefig("out.png")



y1 = [v_square*m*floor(i) for i in x]
y2 = [v_round*n_hex(i,m) for i in x]

y3 = []
for i in range(len(y1)):
    y3.append((lambda a,b: a/b if b != 0 else 0)(y1[i],y2[i]))

plt.title("Ratio of Square vs Round Doughnut Volume per Box")
plt.xlabel("Box Length (n)")
plt.ylabel("(V_square / V_round)")
plt.plot(x,y3)
plt.show()

