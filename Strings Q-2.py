#Print true if the string contains all numeric characters.
a=input("Enter a string")
l=len(a)
flag=0
for i in range(l):
    if(a[i].isdigit()==False):
        flag=1
if(flag==0):
    print("True")
else:
    print("False")
