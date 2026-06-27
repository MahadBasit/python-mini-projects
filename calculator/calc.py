def main():
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
        
            print(calc(num1, num2, op))
            con = input('Do you want to continue: ').upper()
            if con == 'NO':
                break

        except ValueError:
            print('Invalid input(s)')
        except ZeroDivisionError:
            print('Cannot divide by 0')

def calc(n1, n2, op):

    if op == '+':
         return n1 + n2

    elif op == '-':
        return n1 - n2

    elif op == '*':
        return n1 * n2

    else:
        return n1 / n2
    
if __name__ == "__main__":
    main()