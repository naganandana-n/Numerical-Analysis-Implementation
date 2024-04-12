def bisectionMethod(func, a, b, errorAccept):
    """
    func: user defined function - string
    a: lower root boundary
    b: upper root boundary
    errorAccept: user's acceptable level of error
    """
    def f(x):
        f = eval(func)
        return f
    
    error = abs(b - a)

    while error > errorAccept:
        c = (b + a) / 2

        if f(a) * f(b) >= 0:
            print("No root / multiple roots present")
            quit()

        elif f(c) * f(a) < 0:
            b = c
            error = abs(b - a)

        elif f(c) * f(b) < 0:
            a = c
            error = abs(b - a)
        
        else:
            print("Something went wrong")
            quit()
    
    print(f"The error is {error}")
    print(f"The lower boundary, a, is {a} and the upper boundary, b, is {b}")


# function call

bisectionMethod("(4*x ** 3)  + 3*x - 3", 0, 1, 0.05)
