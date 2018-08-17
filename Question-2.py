''' Add the following list to above created list: 
[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]'''
l=[]
n=int(input("Enter size of list"))
for i in range(n):
    inp=input("Enter element")
    l.append(inp)
list2=['google','apple','facebook','microsoft','tesla']
l.extend(list2)
print(l)
