def factorial(n):
    cfact = 1
    for i in range(1, n + 1):
        cfact *= i
    return cfact
sample = 5
fact = factorial(sample)
print(f"Factorial of {sample} is: {fact}")
