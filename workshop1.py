operator, numberA,numberB = input("Enter an operator: +,-,*, /;number A and number B")
numberA = int(numberA)
numberB = int(numberB)


def calc (operator,a,b):
    if operator == 'x':
        print(a*b)
    elif operator =='+':
        print(a+b)
    elif operator == '-':
        print(a-b)
    elif operator == '/':
        print(a / b)
    else :
        print("Invalid operator")

calc(operator, numberA, numberB)