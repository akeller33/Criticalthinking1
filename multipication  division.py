# Andrew Keller
# 10/10/24

def main():
    num1 = get_input()
    num2 = get_input()
    a = multiply(num1, num2)
    d = division(num1, num2)
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

def multiply(num1, num2):
    product = num1 * num2
    return product

def division(num1, num2):
     if num2 == 0:
         divided = 'num1 / num2 is undefined since num2 is zero. '
     else:
         divided = num1 / num2
     return divided

def output(product, divided):
    print(f'num1 x num2 is {product:.2f}')
    if isinstance(divided, str):
        print(divided)
    else:
        print(f'num1 / num2 is {divided:.2f}')

if __name__ == '__main__':
    main()









