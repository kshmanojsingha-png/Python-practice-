n=int(input("Enter no of elements you want to enter"))
a=[]
for i in range(n):
    x=int(input("Enter the elements"))
    a.append(x)
print("List is:",a)
x=int(input("Enter the element you want to enter"))
a.append(x)
print("List is:",a)
x=int(input("Enter the element you want insert"))
pos=int(input("Enter the position you want to insert the element"))
a.insert(pos,x)
print("List is:",a)
x=int(input("Enter the element you want remove"))
a.remove(x)
print("List is:",a)
x=int(input("Enter the index of element you want to delete : "))
a.pop(x)
print("List is:",a)
a.sort()
print("List is:",a)
a.reverse
print("List is:",a)
c=a.count(x)
print("List after counting:",a)
x2=int(input("Enter the number you want to find the index : "))
posi=a.index(x2)
print("List is:",a)
x=int(input("Enter the element you want to add"))
b=[1,2,3,4]
a.extend(b)
print("List is:",a)


