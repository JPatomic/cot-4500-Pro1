# Programming Assignment 1
# JP O'Toole
# COT4500

# Imports Math Library
import math

# Q1: Approximation Algorithm

# Defining Variables
x0, tol, i = 1.5, 1e-6, 0
diff, x = x0, x0

# Print First Iteration
print(i, ":", x)

# Loops until within tolerance threshold
while( diff >= tol ):

    # Updates iteration, established y as placeholder for old x, calculates new x
    i += 1
    y = x
    x = (x/2) + (1/x)

    # Prints the current iteration
    print(i, ":", x)

    # Updates check for being within tolerance threshold
    diff = abs(x-y)

# Prints final result
print("\nConvergence after", i, "iterations\n")

# Q2: The Bisection Method

# Defining Variables
a, b, i, tol, max_it = 1, 2, 0, 1e-6, 50

# Loops until within tolerance or max iterations reached
while(abs(b-a) > tol and i < max_it):

    # Updates iterations and establishes midpoint
    i += 1
    p = (a+b) / 2

    # Case for if midpoint is too high
    if p**2 > 2:
        b = p

    # Case for if midpoint is too low
    else:
        a = p

# Prints final results
print(f"{p:.10}\n")


# Q3: The Fixed-Point Iteration

# Defining Variables
p0, tol, max_it, i, p = 1.5, 1e-6, 50, 1, 0
result = "Failure"

# Loops through the iteration count
while(i <= max_it):

    # Establishes the polynomial
    p = p0 - p0*p0*p0 - 4*p0*p0 + 10

    # Checks if number is undefined
    if(math.isnan(p)):
        print("\nResult diverges\n")
        break

    # Prints the result of the test case
    print(i, ":", p)

    # Checks if the tolerance threshold is met
    if(abs(p-p0) < tol):
        result = "Success"
        break

    # Updates variables
    i += 1
    p0 = p

# Prints final results
print(result, "after", i, "iterations\n")


# Q4: The Newton-Raphson Method

# Defining Variables
p1, tol, max_it, i = ((math.pi)/4), 1e-6, 50, 0

# Defining Functions
def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

print(i, ":", p1)

# Loops until max iterations hit
while(i <= max_it):

    # Reiterates through the formula
    if(df(p1)):

        # Updates iterations, polynomial, and prints it out
        i += 1
        p2 = p1 - (f(p1) / df(p1))
        print(i, ":", p2)

        # Ends loop if tolerance threshold is reached
        if(abs(p2 - p1) < tol):
            print(i+1, ":", p2)
            break

        # Updates for next loop
        p1 = p2

    # Prints failure if derivative ends
    else:
        print("Failure, derivative is zero")
        break

# Prints failure if iterations 
if(i > max_it):
    print("Failure, max iterations performed")
        
