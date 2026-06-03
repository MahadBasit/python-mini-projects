def main():
    name = input('What is your name? ')
    fav_num = input('Your favourite number? ')
    hello(name,fav_num)

def hello(name,number):
    print(f'Hello {name}! Your favourite number is {number}')
main()