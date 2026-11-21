def mc():
    print("\nYou have selected the conversion module.")
    print("From which to which conversion do you want?\n")
    print("1) M (meter) to CM (centimeter)")
    print("2) CM (centimeter) to M (meter)")
    print("3) NM (nanometer) to M (meter)")
    print("4) M (meter) to KM (kilometer)")

    try:
        choice = int(input("Enter the selected option: "))
    except ValueError:
        print("Invalid input. Returning to conversion menu.")
        mc()
        return

    if choice == 1:
        val = float(input("Enter the value in M (meter): "))
        res = val * 100
        print(f"The conversion from {val} (meter) to {res} (centimeter) is: {res}")
        exit2_f_module_mc()
    elif choice == 2:
        val = float(input("Enter the value in CM (centimeter): "))
        res = val / 100
        print(f"The conversion from {val} (centimeter) to {res} (meter) is: {res}")
        exit2_f_module_mc()
    elif choice == 3:
        val = float(input("Enter the value in NM (nanometer): "))
        res = val * 1e-9
        print(f"The conversion from {val} (nanometer) to {res} (meter) is: {res}")
        exit2_f_module_mc()
    elif choice == 4:
        val = float(input("Enter the value in M (meter): "))
        res = val / 1000
        print(f"The conversion from {val} (meter) to {res} (kilometer) is: {res}")
        exit2_f_module_mc()
    else:
        print("Invalid option. Returning to conversion menu.")
        mc()


def exit2_f_module_mc():
    ans = input("Do you want to exit? Type yes/y to exit or no/n to continue: ").strip().lower()
    if ans in ("y", "yes"):
        print("Exiting program...")
        exit()
    elif ans in ("n", "no"):
        cc()
    else:
        print("Invalid input. Retrying conversion...")
        mc()


def cc():
    from c import area
    from v import volume
    from d import der
    from i import ite
    from b import basic
    from a import adv
    from main import main

    ans = input("Do you want to quit the program? (yes/y or no/n): ").strip().lower()
    if ans in ("y", "yes"):
        print("You have selected yes to quit the program.")
        exit()
    elif ans in ("n", "no"):
        print("You have selected continue.")
        print("1) Area / return to area menu")
        print("2) Use other functions")
        sub = input("Enter 1 or 2: ").strip()

        if sub == "1":
            area()
        elif sub == "2":
            print("Which function do you want to use?")
            print("1) volume()")
            print("2) der()")
            print("3) ite()")
            print("4) basic()")
            print("5) adv()")
            try:
                fn_choice = int(input("Enter the function number: "))
            except ValueError:
                print("Invalid number. Returning to main menu.")
                main()
                return

            if fn_choice == 1:
                volume()
            elif fn_choice == 2:
                der()
            elif fn_choice == 3:
                ite()
            elif fn_choice == 4:
                basic()
            elif fn_choice == 5:
                adv()
            else:
                print("Invalid option. Returning to main menu.")
                main()
        else:
            print("Invalid option. Returning to main menu.")
            main()
    else:
        print("Invalid confirmation. Returning to main menu.")
        main()