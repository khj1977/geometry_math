import sys
sys.path.append("../")

from package.geometry import diff_integral as d

f = lambda z: z * z

x = 2.0
deltaX = 0.5
ddeltaX = 0.01
thDX = 0.001
while True:
    if deltaX < thDX:
        break
    diff = d.doNumericalDiff(f, x, deltaX)
    print("num diff gradually: " + str(diff))
    deltaX = deltaX - ddeltaX