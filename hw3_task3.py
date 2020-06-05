def my_func(x, y, z):
    m = max((x + y), (x + z), (y + z))
    return m


print(my_func(int(input("Введите число 1 ")), int(input("Введите число 2 ")), int(input("Введите число 3 "))))


# разве вид функции my_func() подразумевает работу с позиционными аргументами?