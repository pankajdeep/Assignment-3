#Count the number of time an object occurs in a list.
l=[]
n=int(input("Enter size of list"))
for i in range(n):
    inp=int(input("Enter element"))
    l.append(inp)
num=int(input("Enter the number you want to find  the count of"))
print(l.count(num))
