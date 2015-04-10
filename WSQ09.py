def factorial(n):
    x = n
    y = 1
    while (x > 1):
        y = y * x
        x = x - 1
    return y
a= "y"
while (a == "y"):
        n = int(input("Type an integer"))
        f = factorial(n)

        if (n < 0):
            print("It mus be positive")
        else:
            print("The factorial of", n, "is", f)
            a = input("Try again? y/n")
