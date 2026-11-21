from module import exit2_f_module_mc


def der():
    print("\nYou have selected Derivative (power rule: d/dx [a * x^n] = a*n * x^(n-1)).")
    try:
        a = float(input("Enter coefficient a: "))
        n = float(input("Enter power n: "))
    except ValueError:
        print("Invalid number.")
        return

    coeff = a * n
    power = n - 1
    print(f"Derivative of {a}*x^{n} is: {coeff}*x^{power}")
    exit2_f_module_mc()