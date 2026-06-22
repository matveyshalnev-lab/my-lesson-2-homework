num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

operation = input("Введіть операцію (+, -, *, /): ")
if operation == "+":
    result = num1 + num2
    print(result)
    if operation == "-":
        result = num1 - num2
        print(result)
        if operation == "*":
            result = num1 * num2
            print(result)
            if operation == "/":
                result = num1 / num2
                print(result)
            else:
                print("Помилка!!! ділення на нуль неможливе")

        else:
            print("П омилка!!! невідома операція")