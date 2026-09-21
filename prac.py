x=10
print(type(x))

y="Hello"
print(type(y))

name = "Python"
greet = 'Hi' + name
print(greet[0])
print(name[::-1])

fruits=["Mango","Grape"]
fruits.append("Banana")
print(fruits)

student = {
    "names" : "Riya",
    "class" : 12,
    "grade" : 35
}
print(student["grade"])
student ["class"] = 10
print(student)

str="25"
store=int(str)
sum=store+5
print(sum)

tup=(6,5,4)
new_tup=tup.append(9)
print(new_tup)

total = 0
for i in range (1,6):
    total += i
print(total)

for fruit in  ["Apple", "Banana"]:
    print(fruit)
n=5 
while(n > 0):
    print(n)
    n-=1
print("Lift off !")

for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)

for i in range(1,21):
    if i % 2 == 0:
        print(i)

sub = 10
add = 1
num = 7
while (sub > 0):
    tab = num * add
    add += 1
    sub -= 1
    print(tab)

num =int(input("Enter the number : "))
change=str(num)
sum=0
while True:
    for i in change:
        sum +=int(i)
    print(sum)
    break

password=input("Enter the Password : ")
if (password!="1234"):
    print("Please enter the password again:")

else:
    print("Correct password")

