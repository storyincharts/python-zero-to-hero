y = int(input("Enter year:"))

if (y % 400 == 0) and (y % 100 == 0):
    print("It's a leap year")
elif (y %  4 == 0) and (y % 100 != 0):
    print("It's a leap year")
else:
    print("It's not a leap year")
