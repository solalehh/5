num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
num4=int(input("Enter fourth number: "))
if num1>num2 and num1>num3 and num1>num4:
    print("num1")
elif num2>num1 and num2>num3 and num2>num4:
    print("num2")
elif num3>num1 and num3>num2 and num3>num4:
    print("num3")
else:
    print("num4")