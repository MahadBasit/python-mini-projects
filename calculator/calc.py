while True:
    try:
        num1 = int(input("Enter a num: "))
        num2 = int(input("Enter another num: "))
        while True:
            op = input("Enter a operation: ")
            if op in ['+', '-', '*', '/']:
                break
            else:
                print("Enter a valid operation")
       
        if op == '/' and num2 == 0:
            print('Cannot divide by zero')
            continue

        elif op == '+':
            result = num1 + num2

        elif op == '-':
            result = num1 - num2

        elif op == '*':
            result = num1 * num2

        else:
            result = num1 / num2
            
        print(result)
        cont = input("Do you want to continue? ").upper()
        if cont == 'NO' or cont == 'N':
            break
             

    except ValueError:
        print("Enter valid numbers")