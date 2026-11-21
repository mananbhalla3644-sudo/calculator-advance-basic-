from module import exit2_f_module_mc


def basic():
    print("\nYou have selected the basic calculator.")
    try:
        x = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /, %): ").strip()
        y = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number.")
        return

    if op == "+":
        print("Result:", x + y)
    elif op == "-":
        print("Result:", x - y)
    elif op == "*":
        print("Result:", x * y)
    elif op == "/":
        print("Result:", "Cannot divide by zero" if y == 0 else x / y)
    elif op == "%":
        print("Result:", "Cannot modulo by zero" if y == 0 else x % y)
    else:
        print("Invalid operator.")

    exit2_f_module_mc()