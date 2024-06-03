from com_gmail_eulerbonjour.digital_signal import z_transform as z
import math as m

r = 1.0
wt = 0.0

deltaWt = 0.01

# nBegin = -1000.0
# nBegin = -100.0
nBegin = 0.01
nEnd = 100.0

theta = 0.0
deltaTheta = 0.01
i = nBegin
iMax = 100
xn = []
while True:
    if (i > nEnd):
        break

    sin = m.sin(theta) + m.sin(100 * theta)
    xn.append(sin)

    theta = theta + deltaTheta
    i = i + 1

while True:
    if (r > 3.0):
        break
    while wt < 6.28:
        if (wt > 6.28):
            break

        xz = z.calcZTransOverN(xn, r, wt, nBegin, nEnd)
        power = z.calcPowerOfZ(xz)

        # print(str(r) + "," + str(wt) + "," + str(xz[0]) + "," + str(xz[1]))
        print(str(r) + "," + str(wt) + "," + str(power))
        # print(power)
        # print(str(wt) + "," + str(power))

        wt = wt + deltaWt
    r = r + 0.1
    wt = 0.0