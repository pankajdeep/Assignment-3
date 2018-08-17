'''Given are two one-dimensional arrays A and B which are sorted in ascending order.
Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]'''
A=[9,11,3,5,4]
B=[13,27,7,2,1]
A.sort()
B.sort()
C=[]
C.extend(A)
C.extend(B)
C.sort()
print(C)
