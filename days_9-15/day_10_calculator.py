import operator

operations = {"+": operator.add,
              "-": operator.sub,
              "*": operator.mul,
              "/": operator.truediv}


def calculator():
    num1 = float(input("What's the first number? "))
    should_continue = True
    while should_continue:
        for _ in operations:
            print(_)
        operation = input("Choose an operation! ")
        num2 = float(input("What's the next number? "))
        result = operations[operation](num1, num2)
        print(f"The calculation of {num1} {operation} {num2} is {result}")
        if input("Proceed with the answer for another calculation - 'Y' or 'N': ").lower() == "y":
            num1 = result
        else:
            if input("Want to use calculator again - 'Y' or 'N': ").lower() == "y":
                should_continue = False
                calculator()
            else:
                should_continue = False
                print("Bye")


calculator()