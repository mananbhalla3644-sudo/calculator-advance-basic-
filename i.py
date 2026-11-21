from module import exit2_f_module_mc


def ite():
    print("\nYou have selected Integration (power rule: ∫ a*x^n dx = (a/(n+1)) * x^(n+1) + C).")
    try:
        a = float(input("Enter coefficient a: "))
        n = float(input("Enter power n (not -1): "))
    except ValueError:
        print("Invalid number.")
        return

    if n == -1:
        print("Integral of a/x is: ln|x| + C")
    else:
        new_power = n + 1
        coeff = a / new_power
        print(f"Integral of {a}*x^{n} is: {coeff}*x^{new_power} + C")

    exit2_f_module_mc()