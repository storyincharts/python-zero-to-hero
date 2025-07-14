n = int(input("Give the value of n: "))

fact = 1

while n>0:
    fact = fact*n
    n-=1
print(fact)