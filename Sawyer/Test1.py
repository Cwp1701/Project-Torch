Num1 = float(input("put in a Number : "))
Num2 = float(input("put in a Number : "))
op = input("put in a operator : ")


def cac(Num1,Num2):
    if op == "+":
        print(Num1 + Num2)
    elif op == "-":
        print(Num1 - Num2)
    elif op == "/":
        print(Num1 / Num2)
    elif op == "*":
        print(Num1 * Num2)
    else:
        print("Invalid operator")


cac(Num1, Num2)
























