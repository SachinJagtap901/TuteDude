a = int(input("Enter a number: "))

def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
result=factorial(a)
print(f"Factorial of {a} is: ",result)
