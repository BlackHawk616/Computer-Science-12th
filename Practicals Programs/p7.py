import math

def sin(x,n):
    sine = 0
    for i in range(n):
        sign = (-1)**i  # Alternating sign
        sine += sign * (x**(2*i + 1)) / math.factorial(2*i + 1)
    return sine

m = int(input("Enter The Degrees : "))
n = int(input("Enter The Number Of Terms : "))
x = math.radians(m) 
print(sin(x, n))