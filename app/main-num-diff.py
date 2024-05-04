from com_gmail_eulerbonjour.geometry import diff_integral as d

f = lambda z: z * z

diff = d.doNumericalDiff(f, 2.0, 0.001)
print("num diff: " + str(diff))