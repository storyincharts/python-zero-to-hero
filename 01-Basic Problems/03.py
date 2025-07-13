## Solving Quadratic Equation
#sample input: a=1, b=-3, c=2 , output: Roots:(2.0,1.0)

a = int(input("Give a:"))
b = int(input("Give b:"))
c = int(input("Give c:"))

d = (b**2) - (4*a*c)
e = d**0.5
f = 2*a

root1 = (-b+e)/f
root2 = (-b-e)/f

print(f"Roots:({root1},{root2})")
