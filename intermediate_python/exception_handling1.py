"""_summary_
this is exception handling problem 1 
"""

num1 = int(input("enter numerator:"))
num2 = int(input("enter denominator:"))

try:
    result = num1 / num2
    print(result)


except ZeroDivisionError:
    print("number cannt be divided by zero")
