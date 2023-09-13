result = None
operand = None
operator = None
wait_for_number = True

while True:

    char = input("Type a number, or '=' for result: ")
    result = 0
    
    if char == "=":
       print(f"Calculation result is: {result}")
       break

    elif wait_for_number:
    
        try:
            operand = char
            operand = int(operand) if operand.isdigit() else float(operand)
            print(f"operand is: {operand}, operand type is: {type(operand)}")
            # if operand.isdigit():
            #     operand = int(operand)
            # else:
            #     operand = float(operand)
        except ValueError:
            print(f"{operand} is not a number. Try again...")
        wait_for_number = False
    else:
        char = input("Chose operator: '+' or '-' or '/' or '*':")
        if char not in ('+','-','/','*'):
            print(f"{char} is not a '+' or '-' or '/' or '*'. Try again...")
            continue
        operator = char
        if operator == "+":
            result += operand
            wait_for_number = True
        elif operator == "-":
            result -= operand
            wait_for_number = True
        elif operator == "*":
            result *= operand
            wait_for_number = True
        else:
            if operand == 0:
                print(f"Devision by {operand} is not allowed")
                continue
            result /= operand
            wait_for_number = True
        
    
    # operator = input("Please input operator")
    # try:
    #     if operator not in ("+","-","/","*"):
    #         if operator == "+":
    #             result += operand
    #             print(f"operator is {operator}")
    #         elif operator == "-":
    #             result -= operand
    #             print(f"operator is {operator}")
    #         elif operator == "*":
    #             result *= operand
    #             print(f"operator is {operator}")
    #          elif operator == "/":
    #             if operand == 0:
    #                 print("Devision by zero is not allowed")
    #                 continue
    #             result /= operand
    #             print(f"operator is {operator}")
    #         else:
    #             continue          
    #         print(result)
    # except:
    #     print(f"{operator} is not a '+' or '-' or '/' or '*'. Try again...")
                
       