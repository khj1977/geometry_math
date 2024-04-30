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
    # f is assumed to be the same direction with deltaL
    x = 0.0
    while(True):
        if (x > x2):
            break
        diffX = doNumericalDiff(f, x, deltaX)
        smallLine = diffX * deltaL
        sum = sum + smallLine

        x = x + deltaX
    
    return sum

# This algo is under thought and prototype. 
# There might be miss understanding of
# a method of interal of vector over line s. It would be examined
# critically later on.
# It may be speed potential for some occasion.
def doNumericalLineIntegralByVector(fv, fs, x1v, sv, endSv, deltaSv):
    # xv is function is ds
    xv = x1v

    # init by appropriate val?
    dxv = np.array(0.0, 0.0)
    dsv = np.array(0.0, 0.0)

    thS = 0.01

    sum = 0.0
    while True:
        if (sv[0] - endSv[0]) < thS and (sv[1] - endSv[1]) < thS:
            break
        
        dxds = np.dot(dxv, dsv)

        sum = sum + dxds

        xv[0] = fv[0](sv)
        xv[1] = fv[1](sv)

        dsv[0] = fs[0](sv)
        dsv[1] = fs[1](sv)

        sv[0] = sv[0] + dsv[0]
        sv[1] = sv[1] + dsv[1]

    return sum


def doNumericalIntegration(f, x1, x2, deltaX):
    sum = 0.0
    x = x1

    while True:
        if (x > x2):
            break

        f1 = f(x)
        f2 = f(x + deltaX)

        square = (f1 + f2) * deltaX / 2.0

        sum = sum + square

        x = x + deltaX

    return sum

def calcTaylorSeries(f, fDot, x0, x):
    # f = x0, x:
    y0 = f(x0, x)
    y1 = fDot(x0, x) * (x - x0)

    y = y0 + y1
    
    return y