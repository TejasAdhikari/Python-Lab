while 1:
    A = int(input("Enter a Number"))
    if 0<A<=1000:
        break
    else:
        print("Invalid Input")
for b in range (1, A):
    for a in range (1, b+1):
        if a**2+b**2 == A:
            print(a, b)