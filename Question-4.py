#create a list with numbers and sort it in ascending order.
l=[]
n=int(input("Enter size of list"))
for i in range(n):
    inp=int(input("Enter element"))
    l.append(inp)
print("Original list :",l,"\n")
l.sort()
print("Sorted list :",l)
