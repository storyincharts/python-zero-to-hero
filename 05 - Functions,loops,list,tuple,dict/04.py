## input = 1,2,3,2,1,4,2,5
inp = input().split(",")

l = [int(item) for item in inp]

n = int(input())

# count = 0

# for i in l:
#     if i == n:
#         count += 1

## simple methon without for loop
c = l.count(n)

print(count)