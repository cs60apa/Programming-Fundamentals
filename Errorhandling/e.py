
x = int(input("Enter a number: "))
try:
    print("The result is:", 10 / x)
except ZeroDivisionError:
    print("You cannot divide by zero!")