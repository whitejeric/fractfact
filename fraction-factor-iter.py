import itertools
import sys

for p in range(1,6):
    goal = p
    print(("-" *5) + "GOAL:" + str(goal) + ("-" *5) + "\n")
    flips = []
    maxE = 10
    maxr = 24
    noSol = True
    while(maxr < maxr + maxE and noSol): #longer strings
        print("range=" + str(goal+1)+ " to " + str(maxr))
        best = ["n/a", "--", "--", "--"] #x, binary, fraction expansion, num of multiples
        shortestMult = 1000
        A = list(range(goal+1, goal+maxr, 1))
        B = list(range(goal+2, goal+ 2 + maxr, 1))
        flipped = ["".join(seq) for seq in itertools.product("01", repeat=len(A))]
        print(len(flipped))
        flips = flipped
        x = 0.0
        eps = 0.5

        i =0
        j=0
        a=1
        b=1
        frac = ""
        while (i < len(flips)): #new string of binary
            stri = " ".join(flips[i])
            F = [int(s) for s in stri.split() if s.isdigit()]
            for j in range(0, len(F)): #calculate
                a *= A[j]*F[j] + B[j]*(1 - F[j])
                b *= B[j]*F[j] + A[j]*(1 - F[j])
                x = a/b
                if(isinstance(x, int) and x < a and x < b):
                    print("INTERESTING!")
                if (goal + eps >= x and x >= goal - eps and j < shortestMult):
                    for k in range(0, j+1):
                        if (F[k] == 1):
                            frac += "("+str(A[k]) + "/" + str(B[k]) + ") "
                        else:
                            frac += "("+str(B[k]) + "/" + str(A[k]) + ") "
                    epsString = "%.9f" % eps
                    frac+= " = " +str(a/b) + ", epsilon=" + epsString
                    eps = abs(x - goal)
                    if (x == goal and j < shortestMult):
                        best[0] = str(a/b)
                        best[1] = stri
                        best[2] = frac
                        best[3] = "multiple count=" + str(j + 1)
                        shortestMult = j
                        print ("ahh!")
                        print(best)
                        noSol = False
                    elif (noSol):
                        best[0] = str(a/b)
                        best[1] = stri
                        best[2] = frac
                        best[3] = "multiple count=" + str(j + 1)
                    frac = ""
            a = 1
            b = 1
            x = 0
            i+=1
        if(noSol):
            print(best)
            noSol = True
        maxr+=1
        print(i)

# GOAL=1
#
# range=2 to 20
# 524288
# ahh!
# ['1.0', '0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0', '(2/3) (3/4) (4/5) (5/6) (7/6) (8/7) (9/8) (10/9) (11/10) (12/11) (13/12) (14/13) (15/14) (16/15) (17/16) (18/17)  = 1.0, epsilon=0.005917160', 'multiple count=16']
# ahh!
# ['1.0', '0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0', '(3/2) (4/3) (4/5) (5/6) (6/7) (7/7)  = 1.0, epsilon=0.000000000', 'multiple count=6']
# 524288
# ===================================
# GOAL=2
#
# range=3 to 20
# 524288
# ahh!
# ['2.0', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', '(3/4) (4/5) (5/6)  = 2.0, epsilon=0.333333333', 'multiple count=3']
# 524288
# ===================================
# GOAL=3
#
# range=4 to 20
# 524288
# ahh!
# ['3.0', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', '(4/5) (5/6) (6/7) (7/8) (8/9) (9/10) (10/11) (11/12)  = 3.0, epsilon=0.250000000', 'multiple count=8']
# 524288
# ===================================
# GOAL=4
#
# range=5 to 20
# 524288
# ahh!
# ['4.0', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', '(5/6) (6/7) (7/8) (8/9) (9/10) (10/11) (11/12) (12/13) (13/14) (14/15) (15/16) (16/17) (17/18) (18/19) (19/20)  = 4.0, epsilon=0.200000000', 'multiple count=15']
# 524288
