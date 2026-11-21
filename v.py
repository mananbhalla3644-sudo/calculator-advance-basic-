import math
from module import exit2_f_module_mc


def volume():
    print("\nYou have selected Volume.")
    print("1) Cube")
    print("2) Cuboid")
    print("3) Sphere")
    print("4) Cylinder")
    print("5) Cone")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice == 1:
        a = float(input("Enter side length: "))
        print("Volume of cube:", a ** 3)
    elif choice == 2:
        l = float(input("Enter length: "))
        b = float(input("Enter breadth: "))
        h = float(input("Enter height: "))
        print("Volume of cuboid:", l * b * h)
    elif choice == 3:
        r = float(input("Enter radius: "))
        print("Volume of sphere:", (4 / 3) * math.pi * (r ** 3))
    elif choice == 4:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        print("Volume of cylinder:", math.pi * (r ** 2) * h)
    elif choice == 5:
        r = float(input("Enter radius: "))
        h = float(input("Enter height: "))
        print("Volume of cone:", (1 / 3) * math.pi * (r ** 2) * h)
    else:
        print("Invalid choice.")

    exit2_f_module_mc()