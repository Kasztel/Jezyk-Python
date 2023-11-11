def factorial(n):
    if n < 0:
        raise ValueError("Correct input: n>=0")
    fin = 1
    for i in range(1,n+1):
        fin *= i
    return fin



print(factorial(2))
print(factorial(5))
print(factorial(15))
print(factorial(-3))
