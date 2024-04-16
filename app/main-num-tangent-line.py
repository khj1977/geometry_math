import sys
sys.path.append("../package/")

from com_gmail_eulerbonjour.geometry import manifold as ma

f = lambda z: z * z

formedTangentLine = ma.doCalcFormedTangentLine(f, 1.0, 2.0, 0.001, 3.0, 4.0)
print("formed tangent line: " + str(formedTangentLine))