# Andrew Keller
# 10/10/24


def main():
    num1 = get_input()
    num2 = get_input()
    a = addition(num1, num2)
    d = subtraction(num1, num2)
    output(a, d)




def get_input():
    num = input('Enter a number. ')
    while isinstance(num, str):
        if '.' in num:
            while num.count('.') > 1:
                num = input('Input entered was not a number. Enter your a number. ')
            a = num.replace('.','')
        else:
            a = num
        if a.isdigit():
            num = float(num)
        else:
            num = input('Input entered was not a number. Enter a number.')
    return num

def addition(num1, num2):
    sum_of_numbers = num1 + num2
    return sum_of_numbers

def subtraction(num1, num2):
    difference = num1 - num2
    return difference

def output(sum_of_numbers, difference):
    print(f'num1 + num2 is {sum_of_numbers:.2f}')
    print(f'num1 - num2 is {difference:.2f}')
    

if __name__ == '__main__':
    main()
