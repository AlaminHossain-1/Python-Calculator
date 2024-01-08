
def addition():
    num2 = float(input("2nd Number: "))
    result=num1+num2
    print("{0}+{1}={2}".format(num1,num2,result))

def substraction():
    num2 = float(input("2nd Number: "))
    result=num1-num2
    print("{0}-{1}={2}".format(num1,num2,result))

def multipication():
    num2 = float(input("2nd Number: "))
    result=num1*num2
    print("{0}*{1}={2}".format(num1,num2,result))

def division():
    num2 = float(input("2nd Number: "))
    if num2 == 0.0:
        print(num1, "Can't do divide by", num2)
    else:
        result=num1/num2
        print("{0}/{1}={2}".format(num1, num2, result))

def floor_division():
    num2 = float(input("2nd Number: "))
    if num2 == 0.0:
        print(num1, "Can't do divide by", num2)
    else:
        result=num1//num2
        print("{0}//{1}={2}".format(num1, num2, result))

def remainder():
    num2 = float(input("2nd Number: "))
    if num2 == 0.0:
        print(num1, "Can't do divide by", num2)
    else:
        result=num1%num2
        print("{0}%{1}={2}".format(num1, num2, result))

def power():
    num2 = float(input("Power: "))
    result=num1**num2
    print("{0} power {1}={2}".format(num1, num2, result))

def root():
    result=num1**0.5
    print("root {0}={1}".format(num1, result))

while True:
    print("{(+)=addition, (-)=substraction, (*)=multipication, (/)=division, (//)=floor_division, (%)=remainder, (^)=power, (/^)=root}")

    num1=float(input("1st Number: "))
    operator=input("operator: ")

    if operator == '+':
        addition()  
    elif operator == '-':
        substraction()
    elif operator == '*':
        multipication()
    elif operator == '/':
        division()
    elif operator == '//':
        floor_division()
    elif operator == '%':
        remainder()
    elif operator == '^':
        power()
    elif operator == '/^':
        root()

    else:
        print("Invalid choice")
