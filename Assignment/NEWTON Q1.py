"""
Suppose you are designing a roller coaster track, and you need to determine the height of a loop 
at a certain distance along the track to ensure that the roller coaster has enough velocity to 
complete the loop without falling off. The height of the loop at a distance x along the track can 
be modeled by the function:

f(x) = x**3 - x - 1

You want to find the distance x at which the height of the loop reaches a critical value, 
say 20 meters. Use Newton's method to find the distance x at which the height of the loop 
equals 20 meters, given that the initial guess for x is 1.5 meters. 
Additionally, plot the roller coaster track's height function and the tangent lines generated 
during each iteration of Newton's method to visualize the convergence to the solution.
"""


import numpy as np
import matplotlib.pyplot as plt

def newtonMethod(func, funcderiv, x, n):

    def f(x):
        return eval(func)

    def df(x):
        return eval(funcderiv)
    
    roots = []

    for _ in range(n):
        x_next = x - (f(x)/df(x))
        roots.append(x_next)
        x = x_next

    print(f"The root was found to be at {x} after {n} iterations")

    # Plotting the function and tangent lines
    x_vals = np.linspace(min(roots) - 1, max(roots) + 1, 100)
    y_vals = f(x_vals)  # Evaluate the function at x_vals
    tangent_lines = []

    for root in roots:
        tangent_lines.append(df(root) * (x_vals - root) + f(root))

    plt.plot(x_vals, y_vals, label='Function')
    for line in tangent_lines:
        plt.plot(x_vals, line, '--', alpha=0.5)
    plt.scatter(roots[-1], f(roots[-1]), color='red', label='Root')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Newton\'s Method')
    plt.legend()
    plt.grid(True)
    plt.show()

newtonMethod("x**3 - x - 1", "3*x**2 - 1", 1.5, 4)
