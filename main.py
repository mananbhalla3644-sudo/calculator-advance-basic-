from module import mc, exit2_f_module_mc, cc
from c import area
from v import volume
from d import der
from i import ite
from b import basic
from a import adv


def main():
    while True:
        print("\nWelcome to the calculator!")
        print("Menu:")
        print("1) Area")
        print("2) Volume")
        print("3) Derivative")
        print("4) Integration")
        print("5) Advanced equation solver")
        print("6) Basic calculator")
        print("7) Measurement conversion")
        print("8) Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            area()
        elif choice == "2":
            volume()
        elif choice == "3":
            der()
        elif choice == "4":
            ite()
        elif choice == "5":
            adv()
        elif choice == "6":
            basic()
        elif choice == "7":
            mc()
        elif choice == "8":
            print("Exiting calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()