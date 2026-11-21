import math
from module import exit2_f_module_mc


def adv():
    print("\nYou have selected Advanced Equation Solver (Quadratic: ax^2 + bx + c = 0).")
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
    except ValueError:
        print("Invalid input.")
        return

    if a == 0:
        if b == 0:
            print("Not a valid equation.")
        else:
            print("Linear root x =", -c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            r1 = (-b + math.sqrt(d)) / (2 * a)
            r2 = (-b - math.sqrt(d)) / (2 * a)
            print(f"Two real roots: x1 = {r1}, x2 = {r2}")
        elif d == 0:
            r = -b / (2 * a)
            print(f"One real root: x = {r}")
        else:
            real = -b / (2 * a)
            imag = math.sqrt(-d) / (2 * a)
            print(f"Complex roots: {real} + {imag}i and {real} - {imag}i")

    exit2_f_module_mc()