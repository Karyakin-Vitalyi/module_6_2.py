# Домашнее задание по теме "Доступ к свойствам родителя. Переопределение свойств"

class Vehicle:
    __COLOR_VARIANTS = ['BLUE', 'RED', 'GREEN', 'BLACK', 'WHITE']

    def __init__(self, owner, model, color, horsepower):
        self.owner = owner
        self.__model = model
        self.__engine_power = horsepower
        self.__color = color

    def get_model(self):
        return "Модель: " + self.__model

    def get_horsepower(self):
        return "Мощность двигателя: " + str(self.__engine_power)

    def get_color(self):
        return "Цвет: " + self.__color

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print("Владелец: " + self.owner)

    def set_color(self, new_color):
        if new_color.upper() in self.__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print("Нельзя сменить цвет на " + new_color)


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, horsepower):
        super().__init__(owner, model, color, horsepower)


vehicle1 = Sedan('Кирилл', 'BMW 525i e 39', 'BLACK', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызываем методы)
vehicle1.set_color('PINK')
vehicle1.set_color('WHITE')
vehicle1.owner = 'Захар'

# Проверяем что поменялось
vehicle1.print_info()




