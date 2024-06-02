from com_gmail_eulerbonjour.digital_signal import z_transform as z
import math as m

# def calcZTransOverN(r, wt, nBegin, nEnd)

r = 1.0
wt = 0.0

deltaWt = 0.01

nBegin = -1000.0
nEnd = 1000.0

theta = 0.0
deltaTheta = 0.01
i = nBegin
iMax = 100
xn = []
while True:
    if (i > nEnd):
        break

    sin = m.sin(theta)
    xn.append(sin)

    theta = theta + deltaTheta
    i = i + 1

while True:
    if (wt > 6.28):
        break

    xz = z.calcZTransOverN(xn, r, wt, nBegin, nEnd)

    print(str(r) + "," + str(wt) + "," + str(xz[0]) + "," + str(xz[1]))

    wt = wt + deltaWt
