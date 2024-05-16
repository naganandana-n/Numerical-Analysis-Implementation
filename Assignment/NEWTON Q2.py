"""
Suppose you are managing a manufacturing plant, and you need to optimize the production process to minimize costs. The total cost C(x) of producing x units of a product can be modeled by the equation:

C(x) = x^3 + 2 * x^2 + x - 1 

where:

x is the number of units of the product produced.

You want to find the production quantity x that minimizes the total cost C(x). Use Newton's method to find the production quantity x that minimizes the total cost, given that the initial guess for x is x0 = 0.5 units. Additionally, plot the total cost function C(x) and the tangent lines generated during each iteration of Newton's method to visualize the convergence to the solution.
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

newtonMethod("x**3 + 2*x**2 + x - 1", "3*x**2 + 4*x + 1", 0.5, 3)
