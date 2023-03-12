 
try:

    num = int(input("enter muber: "))
    print(num)
    x = 1/0
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)

    print("test")