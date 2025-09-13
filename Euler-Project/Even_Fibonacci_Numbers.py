""" 
Considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

def sum_even_fibonacci(end):
    a, b = 1, 2  
    sum = 0
    
    while a <= end:
        if a % 2 == 0: 
            sum += a
        a, b = b, a + b  # Assigning New Number 
    
    return sum

# Printing Even Fibonacci numbers below 4,000,000
result = sum_even_fibonacci(4000000)
print(f"Sum of even Fibonacci numbers below 4,000,000: {result}")
