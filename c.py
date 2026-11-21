import math
from module import exit2_f_module_mc


def _get_number(prompt, data_type):
    if data_type.lower() == "i":
        return int(input(prompt))
    return float(input(prompt))


def area():
    print("\nYou have selected Area.")
    print("Please choose a shape from the sub-menu:")
    print("1) Circle")
    print("2) Square")
    print("3) Rectangle")
    print("4) Sphere (surface area)")
    print("5) Cone (total surface area)")
    print("6) Cube (surface area)")
    print("7) Cuboid (surface area)")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice.")
        return

    dtype = input("For float type 'f' and for integer type 'i': ").strip()

    if choice == 1:
        r = _get_number("Enter the radius of the circle: ", dtype)
        confirm = input("Confirm value? (yes/y or no/n): ").strip().lower()
        if confirm in ("yes", "y"):
            res = math.pi * (r ** 2)
            print(f"Area of the circle is: {res}")
        exit2_f_module_mc()

    elif choice == 2:
        side = _get_number("Enter the side of the square: ", dtype)
        res = side ** 2
        print(f"Area of the square is: {res}")
        exit2_f_module_mc()

    elif choice == 3:
        length = _get_number("Enter the length of the rectangle: ", dtype)
        width = _get_number("Enter the width of the rectangle: ", dtype)
        res = length * width
        print(f"Area of the rectangle is: {res}")
        exit2_f_module_mc()

    elif choice == 4:
        r = _get_number("Enter the radius of the sphere: ", dtype)
        res = 4 * math.pi * (r ** 2)
        print(f"Surface area of the sphere is: {res}")
        exit2_f_module_mc()

    elif choice == 5:
        r = _get_number("Enter the radius of the cone: ", dtype)
        l = _get_number("Enter the slant height of the cone: ", dtype)
        res = math.pi * r * (r + l)
        print(f"Total surface area of the cone is: {res}")
        exit2_f_module_mc()

    elif choice == 6:
        side = _get_number("Enter the side of the cube: ", dtype)
        res = 6 * (side ** 2)
        print(f"Surface area of the cube is: {res}")
        exit2_f_module_mc()

    elif choice == 7:
        l = _get_number("Enter the length of the cuboid: ", dtype)
        b = _get_number("Enter the breadth of the cuboid: ", dtype)
        h = _get_number("Enter the height of the cuboid: ", dtype)
        res = 2 * (l * b + b * h + h * l)
        print(f"Surface area of the cuboid is: {res}")
        exit2_f_module_mc()

    else:
        print("Invalid shape choice.")