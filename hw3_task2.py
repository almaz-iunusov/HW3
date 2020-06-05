def name_func(name, surname, b_year, city, email, phone):
    print(f"Имя - ​{name}​; Фамилия - ​{surname}​; Год рождения - ​{b_year}​; Город - ​{city}; Электронный адрес - ​{email}​; Номер телефона - {phone}")
    return


name_func(surname=input("Введите фамилию "), name=input("Введите имя"), b_year=input("Введите год рождения "), city=input("Введите город проживания "), email=input("Введите email "), phone=input("Введите номер телефона "))