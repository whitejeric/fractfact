import itertools
import sys


goal = 1
print("goal=" + str(goal))
flips = []
maxr = 25
print("range=" + str(goal+1)+ " to " + str(maxr))
best = ["", "", "", ""] #x, binary, fraction expansion, num of multiples
A = list(range(goal+1, goal+maxr, 1))
B = list(range(goal+2, goal+ 2 + maxr, 1))
flipped = ["".join(seq) for seq in itertools.product("01", repeat=len(A))]
print(len(flipped))
flips = flipped
x = 0.0
eps = 0.001

i =0
j=0
a=1
b=1
frac = ""
while (i < len(flips) and x!=goal):
    stri = " ".join(flips[i])
    F = [int(s) for s in stri.split() if s.isdigit()]
    for j in range(0, len(F)):
        a *= A[j]*F[j] + B[j]*(1 - F[j])
        b *= B[j]*F[j] + A[j]*(1 - F[j])
        x = a/b
        if (goal + eps >= x - eps and x >= goal - eps):
            #print(stri + " == " + str(x))
            print(stri)
            best[0] = str(a/b)
            best[1] = stri
            for k in range(0, j+1):
                if (F[k] == 0):
                    frac += "("+str(B[k]) + "/" + str(A[k]) + ") "
                else:
                    frac += "("+str(A[k]) + "/" + str(B[k]) + ") "
            epsString = "%.9f" % eps
            frac+= " = " +str(a/b) + ", e=" + epsString
            best[2] = frac
            print(frac)
            frac = ""
            eps = abs(x - goal)
            if (x == goal):
                print ("ahh!")
                print(best)
                exit = input("any key to exit")
                if (exit):
                    sys.exit()
    if (x > goal - eps and x < goal + eps):
        print(stri + " == " + str(x))
    a = 1
    b = 1
    x = 0
    i+=1
