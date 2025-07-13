str1 = input("Enter string1:")
str2 = input("Enter string2:")

if len(str1)!=len(str2):
    print("It's not a anagrams")
else:
    if sorted(str1)==sorted(str2):
        print("Strigs are Anagrams")
    else:
        print("It's not a anagrams")

        