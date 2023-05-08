# just here to test random code
# yes it's supposed to be empty (usually)

import math

while True:
    try:
        num = float(input("Enter a number: "))
        if num == 5582:
            print("Em=Ep+Ec")
            print("W= Delta Em ")
            print("Work is sum of conservative and non conservative forces ")
            print("Change in mechanical energy only happens when energy is introduced externally, by non conservative forces like friction, air resistance, simple forces like push or pull")
            print("Ec=1 / 2 x m x v^2 ")
            print("Ep = m x g x h")
            print("W = f x d x cos theta ")
            print("In conservative forces change in mechanical energy is 0 while in FNC it is not 0")
            print("Wfr = Fr x d , Fr = Wfr / d ")
            print("Intensity means calculate force aka magnitude ")
            print("Power is energy / change in time ")
            print("WFNC = Delta Em")
            print("P=W / delta time ")
            print("Weird m is used for performance or efficiency which is e utilised / e total or m (%) = e util / e total and then x100")
            print("1kW=1000W")
            print("1mW=1000kW")
            print("E=P x Delta time ")
            print("Weight (p) = m x g")
            print("W= delta Ec ")
            print("Work total = Work Fr ")
            print("Wfr = Delta Ec ")
            print("Weight is a conservative force, force is conservative if the work done along a closed path where object goes from A to b to A is 0")
            print("In a conservative system Em is constant ")
            print("Em rises when Wfnc > 0 and vice versa ")
            continue
        break
    except ValueError:
        print("Invalid input")

# Arithmetic operations
if num == 25643:
    pass  # do nothing, since we already handled this input above
else:
    while True:
        try:
            op = input("Enter an operator (+, -, *, /, **): ")
            if op not in ['+', '-', '*', '/', '**']:
                print("Invalid operator")
                continue
            num2 = float(input("Enter another number: "))
            break
        except ValueError:
            print("Invalid input")
    if op == '+':
        result = num + num2
    elif op == '-':
        result = num - num2
    elif op == '*':
        result = num * num2
    elif op == '/':
        result = num / num2
    elif op == '**':
        result = num ** num2
    print("Result:", result)
