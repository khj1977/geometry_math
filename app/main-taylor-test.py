import sys
sys.path.append("../package/")

from com_gmail_eulerbonjour.geometry import diff_integral as di
import math as m

# settings
x0 = 0.0

# def doCalcTaylorSeries(f, fDot, x0, x):
f = lambda x0, x: m.sin(x)
fDot = lambda x0, x: m.cos(x)

x = x0
deltaX = 0.0001
endX = 10.0 / 180.0 * 3.14
while True:
    if (x > endX):
        break

    y = di.calcTaylorSeries(f, fDot, x0, x)
    y1 = f(x0, x)

    diff = y - y1

    deg = x / 3.14 * 180.0
    print(str(deg) + "\t" + str(y) + "\t" + str(y1) + "\t" + str(diff))

    x = x + deltaX
