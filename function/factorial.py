given_number= int(input(" Give me a number: "))
def calculateFactorial(input_value):
    nFactorialValue=1

    if input_value == 0:
        return 1
    elif input_value < 0:
        return "factorial calculation of negative numbers is not possible"
    else:
        for i in range (1, input_value +1):
            nFactorialValue *=1
    return nFactorialValue

print(calculateFactorial(given_number))

