'''
This library contains the basic functions that form the basis of the PyNumCore math engine. 
It will handle the fundamental arithmetic operations that all other functions and libraries 
will need to rely on. Note that these are NOT user-facing functions, rather, they are meant 
to be math primitives.

Functions contained in this library:
1. add() --> Finished
2. subtract() --> Finished
3. multiply() --> Finished
4. divide() --> Finished
5. power() --> Finished
6. root() --> Finished
7. absolute_value() --> Finished
8. remainder_c1() --> Finished
9. remainder_c2() --> Finished
10. floor_division() --> Finished
11. reciprocal() --> Finished
12. parts_using_percentage() --> Finished
13. percentage_using_parts() --> Finished
'''

#---------------------------------------------------------------------------------------

'''
Function 1 - The Add Function
Addednds - Note that addends are the name for numbers being added
'''

def add(*addends):
    totalSum = 0

    for addend in addends:
        totalSum += addend

    return totalSum

#---------------------------------------------------------------------------------------

'''
Function 2 - The Subtraction Function
Minuend - The first number / total amount that you start with before taking anything away
Subtrahend - The specific number that is being taken away or subtracted from the minuend
Difference - The final answer or result left over after you subtract
'''

def subtract(minuend, *subtrahends):
    totalDiff = minuend

    for subtrahend in subtrahends:
        totalDiff -= subtrahend

    return totalDiff

#---------------------------------------------------------------------------------------

'''
Function 3 - The Multiplication Function
Factor - Any number that is being multiplied
Product - The result of multiplication
Multiplicand - The number being multiplied 
Multiplier - The number that the multiplicand is being multiplied by
'''

def multiply(multiplicand, *factors):
    totalProduct = multiplicand

    for factor in factors:
        totalProduct *= factor

    return totalProduct

#---------------------------------------------------------------------------------------

'''
Function 4 - The Division Function
Dividend - The number being divided
Divisor - The number we divide the dividend by
Quotient - The result of division
Remainder - What is left over from division if it isn't "clean" or exact
'''

def divide(dividend, *divisors):
    totalQuotient = dividend

    for divisor in divisors:
        totalQuotient /= divisor

    return totalQuotient

#---------------------------------------------------------------------------------------

'''
Function 5 - The Power Function
Base - The number being multiplied by itself
Exponent - The number that tells how many times the base is multiplied by itself
'''

def power(base, *exponents):
    totalPowerResult = base

    for exponent in exponents:
        totalPowerResult **= exponent

    return totalPowerResult

#---------------------------------------------------------------------------------------

'''
Function 6 - The Root Function
Radicand (x) - The number inside the radical
Index (n) - Tells us which root to take
Radicand's Power (m) - The power of the radicand while it is under the root
A radical can be rewritten as a fractional exponent, where the reciprocal of the index becomes the exponent
root(x) = x^((power of x under root) / root's index) = x^(m/n)
'''

def root(radicand, m, index):
    # Error Reminder - Include method to handle an index of 0 
    totalRoot = power(radicand, (m / index))

    return totalRoot

#---------------------------------------------------------------------------------------

'''
Function 7 - The Absolute Value Function
The absolute value is the distance a number is from 0 on a number line
The absolute value of 5 and -5 for example would be 5 regardless
'''

def absolute_value(num):
    # Think of a number line, we need to meaure the amount of untis a giver number is from zero
    absoluteValue = 0

    # Filter statement for determing if a number is negative or positive and which side of the number line it is on
    if num > 0:
        #num is positive
        # for unit in range(0, num):
        #     absoluteValue += 1
        absoluteValue = num
    elif num < 0:
        #num is negative
        # for unit in range(num, 0):
        #     absoluteValue += 1
        absoluteValue = num * -1

    return absoluteValue 

#---------------------------------------------------------------------------------------

'''
Functions 8 and 9 - The Remainder Function
The Remainder is the left over result from division
Example: 17 / 5 = 3 Whole Groups of 5 with a Remainder 2
We subtract the divisor from the dividend untill we get a number less than the divisor
For negative numbers -> dividend = (divisor * whole-number quotient) + remainder
Example: -17 / 5 = 3 Whole Groups of -5 with a Remainder 2 but 2 is negative in order to get to -17 from -15
-17 = (5 * -3) - 2

Convention 1 - We use magnitude for the division then apply the sign of the dividend to the remainder
Convention 2 - We use the a = bq + r and r = a - bq and floor division 

The convention 1 function is slower than convention 2 because it utilizes a while loop rather than the equation directly
'''

def remainder_c1(num1, num2):
    remainder_value = absolute_value(num1)
    divisor = absolute_value(num2)

    if divisor == 0:
        return "Undefined"
    else:
        while remainder_value >= divisor: # Slower than convention 2
            remainder_value -= divisor

    # if both num1 & num2 are negative, the rule still applies because the negative only cancels for the quotient
    if num1 > 0:
        sign = 1
    else:
        sign = -1

    remainder_value *= sign
    
    return remainder_value

def remainder_c2(num1, num2):
    # Convention 2 Equation --> a = bq + r
    # a - Dividend
    # b - Divisor
    # q - Whole Number Quotient
    # r - Remainder

    if num2 == 0:
        return "Undefined"

    # Round down - Find the greatest integer that is still less than or equal to your number
    floor = num1 // num2

    #r = a - bq
    remainder_value = num1 - (num2 * floor)

    return remainder_value

#---------------------------------------------------------------------------------------

'''
Function 10 - The Floor Division Function
Floor Division is where the result of the division of two numbers is rounded down
to the nearest integer (toward negative infinity). Floor division is useful for finding 
how many complete groups fit into a quantity, without counting a partial group.
'''

def floor_division(num1, num2): # Example: 4.7 (Becomes 4), -4.7 (Becomes -5)
    # Divide num1 and num2 to get result
    # round result down to nearest integer
    # return rounded down result

    if num2 == 0:
        return "Undefined"
    else:
        result = divide(num1, num2) 
        floor_result = int(result) # Example: 4.7 (Becomes 4), -4.7 (Becomes -4)
        # Positive numbers rounded down using type conversion int()
        if floor_result > result:
            floor_result -= 1
            return floor_result
        else:
            return floor_result

#---------------------------------------------------------------------------------------

'''
Function 11 - The Reciprocal Function
The Reciprocal is also known as the multiplicative inverse. It is the number that, when 
multiplied by the original number, produces 1. For a fraction, its reciprocal is found by 
switching the positions of the numerator and denominator. However, a more universal way 
to do it for different values is to divide 1 by the given value to get the reciprocal. 

Example: Whole Number = 4 = 4/1 --> 1 / (4/1) = 1/4 --> 4/1 * 1/4 = 4/4 = 1
Example: Fraction = 3/2 --> 1 / (3/2) = 1/1 * 2/3 = 2/3 --> 3/2 * 2/3 = 6/6 = 1
Example: Decimals = (1/4 = 0.25) --> (1 / 0.25) = (1 / (1/4)) --> 1 / 0.25 = 4 

Zero has no reciprocal
'''

def reciprocal(original_num):
    if original_num == 0:
        return "Undefined | 0 has no reciprocal"
    else:
        reciprocal_num = 1 / original_num

    return reciprocal_num

#---------------------------------------------------------------------------------------

'''
Functions 12 and 13 - The Percentage Functions
Percentage / Percent - A way to express a part of a whole as a fraction out of 100. For example, 
20% means 20 out of 100.

Whole - Original Amount
Percentage - How many parts out of 100
Part - The resulting amount

Part = (Percentage / 100) * Whole
Percentage = (Part / Whole) * 100 --> Won't work if the whole number is zero
'''

def part_using_percentage(whole_num, percentage):
    part = (percentage / 100) * whole_num
    return part

def percentage_using_part(whole_num, part):
    if whole_num == 0:
        return "Undefined | The whole amount cannot be zero"
    percentage = (part / whole_num) * 100
    return percentage
