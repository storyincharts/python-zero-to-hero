## Swap the values of the two variables, without using a temporary variable. 
#Sample input: a =10, b=20, output: a=20,b=10

# If we can do it with Temp variable
# a = int(input("Give a:"))
# b = int(input("Give b:"))
# temp = b
# b = a
# a = temp
# print(f"Value of a is :{a}")
# print(f"Value of a is :{b}")

# if temp variable isn't involved

a = int(input("Give value of a:"))
b = int(input("Give value of b:"))
b = b+a # if we take 5, and 10 as a and b, this is 15
a = b-a # the value of b here is 15, so, 15-5 is 10. i,e a=10
b = b-a # Here the value of b=15, a=10, so, 15-10=5, i,e b=5
print(f"Value of a:{a}") #so when we print a = 10
print(f"Value of b:{b}") # b=5 (Successfully swapped without tem variable)


