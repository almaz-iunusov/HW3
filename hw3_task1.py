def my_funk(*args):
    try:
        arg1 = int(input("Enter first number - "))
        arg2 = int(input("Enter second number - "))
        div = arg1 / arg2
    except ValueError:
        print("Это не число!")
        return
    except ZeroDivisionError:
        print("Делить на ноль нельзя!")
        return
    return div


print(my_funk())
