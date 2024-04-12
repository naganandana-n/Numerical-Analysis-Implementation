def falsePosition(func, a, b, errorAccept):
    """
    func: non linear function given by the user
    a: lower root boundary
    b: upper root boundary
    errorAccept: The level of acceptable error
    return: function returns the approximated root of the non-linear equation between a and b bounds
    """
    def f(x):
        f = eval(func)
        return f
    
    i = 0
    cBefore = 0
    c = (a * f(b) - b * f(a)) / (f(b) - f(a))
    error = abs(c - cBefore)

    while error > errorAccept:

        cAfter = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if f(a) * f(b) >= 0:
            print("No root / multiple roots present")
            quit()

        elif f(cAfter) * f(a) < 0:
            error = abs(cAfter - b)
            b = cAfter
            i = i + 1

        elif f(cAfter) * f(b) < 0:
            error = abs(cAfter - a)
            a = cAfter
            i = i + 1
        
        else:
            print("Something went wrong")
            quit()
        
    print(f"The error remaining is {error}, after {i} iterations")
    print(f"The root can be approximately found at {cAfter}")
    print(f"The lower root boundary, a, is {a}, and the upper root boundary, b, is {b}")
        
falsePosition("(4*x ** 3)  + 3*x - 3", 0, 1, 0.05)