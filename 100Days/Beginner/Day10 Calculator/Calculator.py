import sys







def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": subtract
}


def calculator():
    calc = True
    num1 = float(input("What is the first number?: "))
    for op in operations:
        print(op)

    while calc:
        operation = input("Pick an operation from the list above: ")
        num2 = float(input("What is the second number?: "))




        calculation_function = operations[operation]
        answer = calculation_function(num1, num2)


        print(f"{num1}{operation}{num2} = {answer}")

        again = input("Would you like to continue calculating with the previous answer? 'y' or 'n'\n")

        if again == 'y':
            num1 = answer
        if again == 'n':
            restart = input("Would you like to calculate with a new set of numbers? 'y' or 'n'\n")
            if restart == 'y':
                calculator()
            if restart == 'n':
                sys.exit(0)


calculator()