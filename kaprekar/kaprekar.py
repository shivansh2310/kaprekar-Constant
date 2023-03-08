def kaprekar_recursive(n, previous):
    if n == 0:
        return 0
    
    # Store current n as previous number
    previous = n
    
    # Get the four digits of the given number
    digits = [0] * 4
    for i in range(4):
        digits[i] = n % 10
        n //= 10
    
    # Sort the digits in ascending order and get the number in ascending order
    digits.sort()
    ascending = 0
    for i in range(4):
        ascending = ascending * 10 + digits[i]
    
    # Sort the digits in descending order and get the number in descending order
    digits.sort(reverse=True)
    descending = 0
    for i in range(4):
        descending = descending * 10 + digits[i]
    
    # Get the difference of the two numbers
    difference = abs(ascending - descending)
    
    # If the difference is the same as the previous difference, we have reached Kaprekar's constant
    if difference == previous:
      print("Constant Confirmed")
      print(difference)
      

    elif difference == 0:
      print("Ivalid Number, All digits in the number are the same!")
        
    # Otherwise, recurse with the new difference and previous difference
    return kaprekar_recursive(difference, previous)

def kp(n):
    previous_difference = 0
    return kaprekar_recursive(n, previous_difference)