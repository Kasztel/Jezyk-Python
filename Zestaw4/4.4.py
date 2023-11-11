def fibonacci(n):
    if n < 0:
        raise ValueError("Correct input: n >= 0")
    elif n == 0:
        return 0

    temp1 = 0
    temp2 = 1
    fin = temp2
    for i in range(1, n-1):
        temp1, temp2 = temp2, fin
        fin = temp1 + temp2
    return fin


print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(13))
print(fibonacci(19))
print(fibonacci(-15))


