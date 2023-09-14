result = None
operand = None
operator = None
wait_for_number = True
operator_result = 0
operand_result = 0

while True:
    result = 0
    user_input = input(">>>")
    
    if user_input == "=":
        print(f"result: {result}")
        break
    elif user_input != "=":
        try:
            result += operator_result
            operand = user_input
            operand = int(operand) if operand.isdigit() else float(operand)
            operand_result=result
            print("You are in the operand mode")
        except ValueError:
            print(f"{operand} is not a number. Try again")
        
    else:
        if user_input == "+":
            operator_result = operand_result
            operator_result += operand
        elif user_input == "-":
            operator_result = operand_result
            operator_result -= operand
        elif user_input == "*":
            operator_result = operand_result
            operator_result *= operand
        elif user_input == "/":
            try:
                if operand == "0":
                    continue
            except ZeroDivisionError:
                print(f"Devision by {operand} is not allowed")
        print("you are in the operator mode")

        