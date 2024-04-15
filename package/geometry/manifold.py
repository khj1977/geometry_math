from package.geometry import diff_integral as d
import numpy as np
import math as m

# The idea of tangent space of manifold is impled to think what is tangent space
# and manifold.
# debug
# The following may has numerical bug. Debug later on
# end of debug
def doCalcFormedTangentLine(f, x1, x2, deltaX, p1, p2):
    tangentLineCoeff = d.doNumericalDiff(f, x1, deltaX)
    tangentVector = np.array([x1, x1 + deltaX])
    originalVector = np.array([p1 - x1, p2 - x2])

    cosTheta = m.cos(np.dot(tangentVector, originalVector))
    formedTangentLine = np.array([x1 * cosTheta, (x1 + deltaX) * cosTheta])

    return formedTangentLine