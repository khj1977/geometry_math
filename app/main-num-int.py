import sys
sys.path.append("../")

from package.geometry import diff_integral as d

f = lambda z: z * z

lineIntegral = d.doNumericalLineIntegral(f, 2, 3, 0.001, 0.001)
print("line integral: " + str(lineIntegral))