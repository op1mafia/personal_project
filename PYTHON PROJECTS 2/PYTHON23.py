try:
    value = int(input("enter a number: "))
    print(value)
    result = 10/0
except ZeroDivisionError as error:
    print(error)
except ValueError as error1:
    print(error1)
print("success")