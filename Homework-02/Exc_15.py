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

            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == '/':
                try:
                    result /= operand
                except ZeroDivisionError:
                    print(f"Devision by {operand} is not allowed")
                    continue
                     
          
        except ValueError:
            print(f"{char} is not a number. Try again")
            continue
        wait_for_number = False
        if result == None:
           result = operand

    else:
        if char not in ('+', '-', '*', '/'):
            print(f"Char is not a '+' or '-' or '*' or '/'")
            continue
        operator = char
        wait_for_number = True
# Перша: ["10", "+", "5", "6", "/", "3", "-", "a", "2", "*", "6", "= "], результат 18.0
# Друга: ["2", "3", "-", "1", "+", "10", "*", "2", "="], результат 22.0