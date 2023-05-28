def calculate_physics():
    print("Welcome to the Physics Calculator!")
    print("Choose a variable to calculate:")
    print("1. Current (I)")
    print("2. Voltage (U)")
    print("3. Power of a Purely Resistive Receiver (P)")
    print("4. Energy (E)")
    print("5. Charge (Q)")
    print("6. Time (t)")
    print("7. Velocity (V)")
    print("8. Force (F)")
    print("9. Acceleration (a)")
    print("10. Resistance (R)")
    print("11. Internal Resistance (r)")

    choice = int(input("Enter the number corresponding to the variable: "))

    if choice == 1:
        # Calculation for Current (I)
        print("Choose a formula to calculate Current (I):")
        print("1. I = Q / t (Charge / Time)")
        formula_choice = int(input("Enter the number corresponding to the formula: "))

        if formula_choice == 1:
            Q = float(input("Enter the charge (Q) [C]: "))
            t = float(input("Enter the time (t) [s]: "))
            I = Q / t
            print("Current (I) =", I, "A")
        else:
            print("Invalid formula choice.")

    elif choice == 2:
        # Calculation for Voltage (U)
        print("Choose a formula to calculate Voltage (U):")
        print("1. U = P / I (Power / Current)")
        print("2. U = R * I (Resistance * Current)")
        print("3. U = E / Q (Energy / Charge)")
        formula_choice = int(input("Enter the number corresponding to the formula: "))

        if formula_choice == 1:
            P = float(input("Enter the power (P) [W]: "))
            I = float(input("Enter the current (I) [A]: "))
            U = P / I
            print("Voltage (U) =", U, "V")

        elif formula_choice == 2:
            R = float(input("Enter the resistance (R) [Ω]: "))
            I = float(input("Enter the current (I) [A]: "))
            U = R * I
            print("Voltage (U) =", U, "V")

        elif formula_choice == 3:
            E = float(input("Enter the energy (E) [J]: "))
            Q = float(input("Enter the charge (Q) [C]: "))
            U = E / Q
            print("Voltage (U) =", U, "V")

        else:
            print("Invalid formula choice.")

    elif choice == 3:
        # Calculation for Power of a Purely Resistive Receiver(P)
        print("Choose a formula to calculate Power of a Purely Resistive Receiver (P):")
        print("1. P = U * I (Voltage * Current)")
        print("2. P = E / t (Energy / Delta Time )")
        print("3. P = R * I^2 * t (Resistance * Current Squared * Delta Time) ")
        formula_choice = int(input("Enter the number corresponding to the formula: "))

        if formula_choice == 1:
            U = float(input("Enter the voltage (U) [V]: "))
            I = float(input("Enter the current (I) [A]: "))
            P = U * I
            print("Power (P) =", P, "W")

        if formula_choice == 2:
            E = float(input("Enter the energy (E) [J]: "))
            t = float(input("Enter the time (t) [s]: "))
            P = E / t 
            print("Power (P) =", P, "W")


        if formula_choice == 3:
            R = float(input("Enter the Resistance (Ω) : "))
            I = float(input("Enter the current (I) [A]: "))
            t = float(input("Enter the time (t) [s]: "))
            P = R * I**2 * t   
            print("Power (P) =", P, "W")


        else:
            print("Invalid formula choice.")

    elif choice == 4:
        # Calculation for Energy (E)
        print("Choose a formula to calculate Energy (E):")
        print("1. E = P * t (Power * Time)")
        print("2. E = U * I * t (Voltage * Current * Time)")
        print("3. E = m * g * h (Mass * Gravity * Height)")
        print("4. E = 0.5 * m * v^2 (0.5 * Mass * Velocity^2)")
        print("5. E = U * Q (Voltage * Charge)")
        formula_choice = int(input("Enter the number corresponding to the formula: "))

        if formula_choice == 1:
            P = float(input("Enter the power (P) [W]: "))
            t = float(input("Enter the time (t) [s]: "))
            E = P * t
            print("Energy (E) =", E, "J")

        elif formula_choice == 2:
            U = float(input("Enter the voltage (U) [V]: "))
            I = float(input("Enter the current (I) [A]: "))
            t = float(input("Enter the time (t) [s]: "))
            E = U * I * t
            print("Energy (E) =", E, "J")

        elif formula_choice == 3:
            m = float(input("Enter the mass (m) [kg]: "))
            g = float(input("Enter the acceleration due to gravity (g) [m/s^2]: "))
            h = float(input("Enter the height (h) [m]: "))
            E = m * g * h
            print("Energy (E) =", E, "J")

        elif formula_choice == 4:
            m = float(input("Enter the mass (m) [kg]: "))
            v = float(input("Enter the velocity (v) [m/s]: "))
            E = 0.5 * m * v**2
            print("Energy (E) =", E, "J")


        elif formula_choice == 5:
            U = float(input("Enter the voltage (U) [V]: "))
            Q = float(input("Enter the charge (Q) [C]: "))
            E = U * Q
            print("Energy (E) =", E, "J")



        else:
            print("Invalid formula choice.")

    elif choice == 5:
        # Calculation for Charge (Q)
        print("Choose a formula to calculate Charge (Q):")
        print("1. Q = I * t (Current * Time)")
        formula_choice = int(input("Enter the number corresponding to the formula: "))

        if formula_choice == 1:
            I = float(input("Enter the current (I) [A]: "))
            t = float(input("Enter the time (t) [s]: "))
            Q = I * t
            print("Charge (Q) =", Q, "C")
        else:
            print("Invalid formula choice.")

    elif choice == 6:
        # Calculation for Time (t)
        print("Choose a formula to calculate Time (t):")
        print("1. t = Q / I (Charge / Current)")
        formula_choice = int(input("Enter the number corresponding to the formula: "))

        if formula_choice == 1:
            Q = float(input("Enter the charge (Q) [C]: "))
            I = float(input("Enter the current (I) [A]: "))
            t = Q / I
            print("Time (t) =", t, "s")
        else:
            print("Invalid formula choice.")

    elif choice == 7:
        # Calculation for Velocity (V)
        print("Choose a formula to calculate Velocity (V):")
        # Add the formulas for Velocity (V) here
        print("Coming soon!")

    elif choice == 8:
        # Calculation for Force (F)
        print("Choose a formula to calculate Force (F):")
        # Add the formulas for Force (F) here
        print("Coming soon!")

    elif choice == 9:
        # Calculation for Acceleration (a)
        print("Choose a formula to calculate Acceleration (a):")
        # Add the formulas for Acceleration (a) here
        print("Coming soon!")

    elif choice == 10:
        # Calculation for Resistance (R)
        print("Choose a formula to calculate Resistance (R):")
        print("1. R = V / I (Voltage / Current)")
        formula_choice = int(input("Enter the number corresponding to the formula: "))

        if formula_choice == 1:
            V = float(input("Enter the voltage (V) [V]: "))
            I = float(input("Enter the current (I) [A]: "))
            R = V / I
            print("Resistance (R) =", R, "Ω")

        else:
            print("Invalid formula choice.")

    elif choice == 11:
        # Calculation for Internal Resistance (r)
        print("Choose a formula to calculate Internal Resistance (r):")
        # Add the formulas for Internal Resistance (r) here
        print("Coming soon!")

    else:
        print("Invalid choice.")

try:

    i = 0
    while i < 11:

        calculate_physics()
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        i = i + 1 
except: 

    print("There was an error in your code, perhaps you did not insert your input in the correct format?")
    

