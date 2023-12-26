#  Design a Python function to find the Max of three numbers.

def find_max_of_three(num1, num2, num3):
    # Use conditional statements to compare the numbers and find the maximum..
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# numbers..
number1 = 47
number2 = 80
number3 = 29

result = find_max_of_three(number1, number2, number3)
print(f"The maximum of {number1}, {number2}, and {number3} is: {result}")
