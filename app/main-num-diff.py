import sys
sys.path.append("../")

from package.geometry import diff_integral

f = lambda z: z * z

diff = diff_integral.doNumericalDiff(f, 2.0, 0.001)
print("num diff: " + str(diff))