result = None
operand = None
operator = None
wait_for_number = True

while True:
    char=input(">>>")

    if char == "=":
        print(f"Result is {result}")
        break
    elif wait_for_number:
        try:
            operand = int(char) if char.isdigit() else float(char)
            wait_for_number = False
          
        except ValueError:
            print(f"{operand} is not a number. Try again")
            continue
        if result == None:
           result = operand

    else:
        if char not in ("+", "-", "*", "/"):
            print(f"Char is not a '+' or '-' or '*' or '/'")
            continue
        operator = char
        wait_for_number = True
        if operator == "+":
            result += operand
        elif operator == "-":
            result -= operand
        elif operator == "*":
            result *= operand
        elif operator == "/":
            try:
                if operand == "0":
                    continue
            except ZeroDivisionError:
                print(f"Devision by {operand} is not allowed")