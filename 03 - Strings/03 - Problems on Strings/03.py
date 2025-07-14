s = input("Enter a string:")

reverse = s[::-1] ## this is a slicing way to solve the problem

if reverse  == s:
    print("It is a palindrome")
else:
    print("It is not a palindrome")

