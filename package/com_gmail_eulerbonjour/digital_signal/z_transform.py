import numpy as np
import math as m

def calcZTrans(n, r, wt):
    cos = m.cos(n * wt)
    sin = m.sin(n * wt)

    rDenom = 1.0 / (r ** n) 

    zRe = rDenom * cos
    zIm = rDenom * sin

    XZPartialWithN = np.array([zRe, zIm])

    return XZPartialWithN

def calcZTransOverN(r, wt, nBegin, nEnd):
    xzRe = 0.0
    xzIm = 0.0

    n= nBegin
    while True:
        if (n > nEnd):
            break

        z = calcZTrans(n, r, wt)
        xzRe = xzRe + z[0]
        xzIm = xzIm + z[1]

        n = n + 1.0

    return np.array([xzRe, xzIm])
