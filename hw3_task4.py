"""Здесь представлена фунцкия вида my_funk(x, y),
для возведения исключительно положительного числа в исключительно отрицательную степень.
Необходимо иметь ввиду что используются позиционные аргументы  x и y,
 и первый параметр будет числом возводимым в степень, а второй показателем степени.
 """


def my_funk(x, y):
    if x > 0 and y < 0:
        grad = 1 / x ** abs(y)
    else:
        print("Entered wrong data")
        return
    return grad


print(my_funk(int(input("Enter ONLY positive x ")), int(input("Enter ONLY negative y "))))

"""Второй вариант решения"""

def my_funk(x, y):
    n = 1
    grad = x
    if x > 0 and y < 0:
        while n < abs(y):
            grad = grad * x
            n = n + 1
        res = 1 / grad
        return res
    else:
        print("Entered wrong data")


print(my_funk(int(input("Enter x ")), int(input("Enter y "))))
