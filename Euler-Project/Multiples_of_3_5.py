"""
Sum of all multiples of 3 or 5 below 1000
"""

def sum_of_multiples(n, end):
    # Calculate number of terms: 
    num_terms = (end - 1) // n
    # Arithematic Series formula 
    return n * (num_terms * (num_terms + 1)) // 2

def sum_multiples(num1, num2, end):
    # Sum of multiples of 3 or 5 = sum(3) + sum(5) - sum(15) to avoid double-counting
    return (sum_of_multiples(num1, end) + 
            sum_of_multiples(num2, end) - 
            sum_of_multiples(num1*num2, end)
            )

# Printing the Result 
result = sum_multiples(3,5,1000)
print(f"Sum of multiples of 3 or 5 below 1000: {result}")