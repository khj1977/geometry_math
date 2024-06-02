import numpy as np
import math as m

def calcZTrans(xn, n, r, wt):
    cos = m.cos(n * wt)
    sin = m.sin(n * wt)

    rDenom = 1.0 / (r ** n) 

    zRe = xn[int(n)] * rDenom * cos
    zIm = xn[int(n)] * rDenom * sin

    XZPartialWithN = np.array([zRe, zIm])

    return XZPartialWithN

# z = r * (coswt + isinwt)
def calcZTransOverN(xn, r, wt, nBegin, nEnd):
    xzRe = 0.0
    xzIm = 0.0

    n= nBegin
    while True:
        if (n > nEnd):
            break

        z = calcZTrans(xn, n, r, wt)
        xzRe = xzRe + z[0]
        xzIm = xzIm + z[1]

        n = n + 1

    return np.array([xzRe, xzIm])

def calcPowerOfZ(xz):
    re = xz[0]
    im = xz[1]
    power = m.sqrt(re * re + im * im)

    return power
