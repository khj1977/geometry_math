import sys
sys.path.append("../package/")

from com_gmail_eulerbonjour.geometry import diff_integral as di
import math as m

# settings
x0 = 0.0
x = x0

# def doCalcTaylorSeries(f, fDot, x0, x):
f = lambda x0, x: m.sin(x)
fDot = lambda x0, x: m.cos(x)

x = x0
deltaX = 0.001
endX = 10.0
while True:
    if (x > endX):
        break

    y = di.calcTaylorSeries(f, fDot, x0, x)
    y1 = m.sin(x)

    print(str(y) + "\t" + str(y1) + "\n")

    x = x + deltaX

