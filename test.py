import sys

inputNumber = int(sys.argv[1])


def factorial(inputNumber):
    total = 1
    if (inputNumber <= 0):
        print("You cant input negative number")
        return(0)
    for i in range(1, inputNumber+1):
        total *= i

    print(total)
    return(total)


factorial(inputNumber)
