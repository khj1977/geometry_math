from com_gmail_eulerbonjour.geometry import diff_integral as d

f = lambda z: z * z

integral = d.doNumericalIntegration(f, 3.0, 4.0, 0.001)
print("integral: " + str(integral))