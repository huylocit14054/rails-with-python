import sys


def factorial_cal(num):
    factorial = 1
    # check if the number is negative, positive or zero
    if num < 0:
        result = "Sorry, factorial does not exist for negative numbers"
    elif num == 0:
        result = "The factorial of 0 is 1"
    else:
        for i in range(1, num + 1):
            factorial = factorial*i
        result = factorial
    print(result)
    return result


if(len(sys.argv) < 2):
    print("Usage: python ex.py")
else:
    num = sys.argv[1]
    factorial_cal(int(num))
