num = int(input("Enter a number: "))

if num < 2:
    print(" The number you have entered is a Prime number ")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(" The number you have entered is a Prime number ")
    else:
        print(" The number you have entered is not a Prime number ")