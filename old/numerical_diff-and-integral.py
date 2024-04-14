import numpy as np
import math as m

# f = lambda x: -0.02 * x

def doNumericalDiff(f, x1, deltaX):
    f1 = f(x1)
    f2 = f(x1 + deltaX)

    differntial = (f2 - f1) / deltaX
    
    return differntial

# debug
# The following function may numerical bug. Debug later.
# end of debug
def doNumericalLineIntegral(f, x1, x2, deltaX, deltaL):
    sum = 0.0

    # for x in range(x1, x2, deltaX):
    x = 0.0
    while(True):
        if (x > x2):
            break
        diffX = doNumericalDiff(f, x, deltaX)
        smallLine = diffX * deltaL
        sum = sum + smallLine

        x = x + deltaX
    
    return sum

# debug
# The following function may numerical bug. Debug later.
# end of debug
def doNumericalIntegration(f, x1, x2, deltaX):
    sum = 0.0
    x = x1
    while True:
        if (x > x2):
            break

        f1 = f(x1)
        f2 = f(x1 + deltaX)

        square = (f1 + f2) * deltaX / 2.0

        sum = sum + square

        x = x + deltaX

    return x

# The idea of tangent space of manifold is impled to think what is tangent space
# and manifold.
# debug
# The following may has numerical bug. Debug later on
# end of debug
def doCalcFormedTangentLine(f, x1, x2, deltaX, p1, p2):
    tangentLineCoeff = doNumericalDiff(f, x1, deltaX)
    tangentVector = np.array([x1, x1 + deltaX])
    originalVector = np.array([p1 - x1, p2 - x2])

    cosTheta = m.cos(np.dot(tangentVector, originalVector))
    formedTangentLine = np.array([x1 * cosTheta, (x1 + deltaX) * cosTheta])

    return formedTangentLine

# main

f = lambda x: x * x

diff = doNumericalDiff(f, 2.0, 0.001)
print("num diff: " + str(diff))

x = 2.0
deltaX = 0.5
ddeltaX = 0.01
thDX = 0.001
while True:
    if deltaX < thDX:
        break
    diff = doNumericalDiff(f, x, deltaX)
    print("num diff gradually: " + str(diff))
    deltaX = deltaX - ddeltaX

lineIntegral = doNumericalLineIntegral(f, 1, 2, 0.001, 0.001)
print("line integral: " + str(lineIntegral))

integral = doNumericalIntegration(f, 2, 3, 0.001)
print("integral: " + str(integral))

formedTangentLine = doCalcFormedTangentLine(f, 1.0, 2.0, 0.001, 3.0, 4.0)
print("formed tangent line: " + str(formedTangentLine))