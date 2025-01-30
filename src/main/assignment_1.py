# Programming Assignment 1
# JP O'Toole

# Q1: Approximation Algorithm




# Q2: The Bisection Method

def bisection(tol = 1e-6, max_it = 50):

    a, b, i = 1, 2, 0
    midpoints = []

    for _ in range(max_it):
        i += 1
        m = (a+b) / 2
        midpoints.append

        if abs(m**2 - 2) < tol:
            break

        if m**2 > 2:
            b = m

        else:
            a = m

    return i

approximations = bisection()
print("Number of iterations: )


# Q3: The Fixed-Point Iteration




# Q4: The Newton-Raphson Method
