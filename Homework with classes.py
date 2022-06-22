#1. Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации (отвечающий за добавку к выбираемому лимонаду).
#В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычная газировка».


'''class Soda:

    def __init__(self, supplement):
        self.soda_pop = 'обычная'  # тип газировки
        self.supplement = supplement  # добавка

    def display_info(self):
        print(f"Газировка: {self.soda_pop}  Добавка: {self.supplement}")


first = Soda("Газировка")
first.supplement = 'яблоко'
first.display_info()

second = Soda("Газировка")
second.supplement = 'нет добавки'
second.display_info()'''


#2. Николай – оригинальный человек.
#Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст. Но на этом он не успокоился.
#Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”.
#В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет, а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
#Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то и вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество» или метод «приветствие», то ничего у такого хитреца не получится).
#Для ограничения количества наборов свойств и методов в экземпляре применяется специальный магический атрибут __slots__.


'''class Nikolai:
  __slots__ = ['name', 'age']

    def __init__(self, age, name):
        self.name = name
        if self.name != 'Николай':
            print(f'Я ВООБЩЕ-ТО НИКОЛАЙ! Никакой не {self.name}')
        self.age = age


pers_one = Nikolai('Николай', 20)
pers_two = Nikolai('Макс', 18)
pers_one.something = 'что-то'''


#3. Напишите программу с классом Student, в котором есть три атрибута: name, groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A. Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы конкретного студента. Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы.


'''class Student:
    def __init__(self, name='Иван', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.groupNumber = group_number

    def get_name(self):
        return f'Имя: {self.name}'

    def get_age(self):
        return f'Возраст: {self.age}'

    def get_group_number(self):
        return f'Группа: {self.groupNumber}.'

    def set_name_age(self, name, age):
        self.name = name
        self.age = age
        return f'Имя: {self.name}, Возраст: {self.age}'

    def set_group_number(self, group_number):
        self.groupNumber = group_number
        return f'Группа: {self.groupNumber}.'


Nicolai = Student('Николай', 20, '1012M')
Ivan = Student()
Mary = Student()
Alex = Student('Алекс', 12, '6B')
Minecrafter = Student('Школьник', 9, 'Noob')
print(f'{Nicolai.get_name()} {Nicolai.get_age()} {Nicolai.get_group_number()}')
print(f'Имя: {Ivan.name} Возраст: {Ivan.age} Группа: {Ivan.groupNumber}.')
print(f'{Mary.set_name_age("Мари", 18)} {Mary.set_group_number("python group")}')
print(f'{Alex.get_name()} {Alex.get_age()} {Alex.get_group_number()}')
print(f'{Minecrafter.get_name()} {Minecrafter.get_age()} {Minecrafter.get_group_number()}')'''


#4. Напишите программу с классом Math. Создайте два атрибута — a и b. Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание. При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.


'''class Math:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition (self):
        return self.a + self.b

    def multiplication (self):
        return self.a * self.b

    def division (self):
        return self.a / self.b

    def subtraction (self):
        return self.a - self.b

num = Math(10,2)

print(f'Сложение:{num.addition()}')
print(f'Умножение:{num.multiplication()}')
print(f'Деление:{num.division()}')
print(f'Вычитание:{num.subtraction()}')'''


5.Напишите программу с классом Car. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год). Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». Третий — присвоение автомобилю года выпуска. Четвертый метод — присвоение автомобилю типа. Пятый — присвоение автомобилю цвета.


'''class Car:
    def __init__(self, type, color, year):
        self.type = type
        self.color = color
        self.year = year

    def get_type(self):
        return f'Тип:{self.type}'

    def get_color(self):
        return f'Цвет:{self.color}'

    def get_year(self):
        return f'Год:{self.year}'

    def starting(self):
        return f'Автомобиль заведен'

    def disabling(self):
        return f'Автомобиль заглушен'


opel = Car('Легковой', 'Белый', 1995)
print(f'{opel.starting()}')
print(f'{opel.get_type()} {opel.get_color()} {opel.get_year()}')
print(f'{opel.disabling()}')'''
