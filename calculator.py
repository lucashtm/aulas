operation = input("Type operation (+, -, *, /): ")

while operation != 'exit':
    first_number = int(input("Type first number: "))
    second_number = int(input("Type second number: "))

    if operation == "+":
        print(first_number + second_number)

    if operation == "-":
        print(first_number - second_number)

    if operation == "*":
        print(first_number * second_number)

    if operation == "/":
        print(first_number / second_number)

    if operation == "**":
        print(first_number ** second_number)
    
    operation = input("Type operation (+, -, *, /): ")