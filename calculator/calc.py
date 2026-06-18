while True:
    try:
        num1 = int(input("Enter a num: "))
        num2 = int(input("Enter another num: "))
        while True:
            op = input("Enter a operation: ")
            if op in ['+', '-', '*', '/']:
                break
       
        
        if op == '+':
            result = num1 + num2

        elif op == '-':
            result = num1 - num2

        elif op == '*':
            result = num1 * num2

        else:
            result = num1 / num2
            
        print(result)
        break

    except ValueError:
        pass