# f = lambda x: -0.02 * x

def doNumericalDiff(f, x1, deltaX):
    f1 = f(x1)
    f2 = f(x1 + deltaX)

    differntial = (f2 - f1) / deltaX
    
    return differntial

def doNumericalLineIntegral(f, x1, x2, deltaX, deltaL):
    sum = 0.0

    # for x in range(x1, x2, deltaX):
    x = 0.0
    while(True):
        if (x > x2):
            break
        diffX = doNumericalDiff(f, x, deltaX)
        smallLine = diffX * deltaL
        sum = sum + smallLine

        x = x + deltaX
    
    return sum

f = lambda x: x

diff = doNumericalDiff(f, 2.0, 0.001)
print(diff)

integral = doNumericalLineIntegral(f, 1, 2, 0.001, 0.001)
print(integral)