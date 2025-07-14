a = input()
x,y,z = a.split(",")
num1 = int(x)
num2 = int(y)
num3 = int(z)

if num1>num2:
    if num1>num3:
        print("The largest number:", num1)
    else:
        print("The largest number:", num3)
elif num2>num1:
    if num2>num3:
        print("The largest number:",num2)
    else:
        print("The largest number:", num3)
elif num3>num1:
    if num3>num2:
        print("The largest number:", num3)
    else:
        print("The largest number:", num2)

