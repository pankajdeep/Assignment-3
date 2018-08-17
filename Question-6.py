#Count even and odd numbers in that list.
l=[]
count_even=0
n=int(input("Enter size of list"))
for i in range(n):
    inp=int(input("Enter element"))
    l.append(inp)
for i in range(n):
    if(l[i]%2==0):
        count_even+=1
print(" Total number of Even elements are :",count_even,"\n","Total number of Odd elements are :",n-count_even)
