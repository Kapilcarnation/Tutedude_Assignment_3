import math

x = float(input("Enter a number: "))

if x <= 0:
    print("Pleas enter Positive numbers")
else:
    sqroot = math.sqrt(x)
    
    log = math.log(x)
    
    sine = math.sin(x)
    
    print(f"Square root: {sqroot}")
    print(f"Logarithm: {log}")
    print(f"Sine: {sine}")
