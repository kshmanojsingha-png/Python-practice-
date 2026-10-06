sum = 0

n = int(input("Enter the number up to which you want to find the sum: "))

for num in range(1, n + 1):
    if num % 2 == 0:
        sum = sum + num

print("Sum of even numbers:", sum)