# Easy
# class Cars:
#     name = "BMW"  # Аттрибуты класса
#     color = "Black"
#     count_wheels = 4
#
#     def show_name(self):
#         return self.name
#
#     def show_color(self):
#         return self.color
#
#
# app = Cars()
# print(app.show_color())


# Medium
# class Cars:
#     def __init__(self, name, color, count_wheels):
#         self.name = name
#         self.color = color
#         self.count_wheels = count_wheels
#
#     def show_name(self):
#         return self.name
#
#     def show_color(self):
#         return self.color
#
#     def show_count_of_wheels(self):
#         return self.count_wheels
#
#
# app = Cars("Lexus", "White", 4)
# print("Name: ", app.show_name())
# print("Color: ", app.show_color())
# print("Count of wheels: ", app.show_count_of_wheels())
# print("_____________________________")
# chevrolet = Cars("Chevrolet", "Black", 4)
# print("Name: ", chevrolet.show_name())
# print("Color: ", chevrolet.show_color())
# print("Count of wheels: ", chevrolet.show_count_of_wheels())


class Cars:
    def __init__(self, name, color, count_wheels):
        self.name = name
        self.color = color
        self.count_wheels = count_wheels

    def show_name(self):
        return self.name

    def show_color(self, alter_name):
        name2 = " Mashine"
        return self.color + name2


main_app = Cars("Chevrolet", "Black", 4)


# print(main_app.show_color())
# print("___________")


class Electronics:
    def show_name(self):
        return "Name"


class Metalls:
    def show_name(self):
        return "Black"


class BMW(Electronics, Cars, Metalls):
    lyuk = True

    def show_color(self, alter_name):
        response = super().show_color(alter_name)
        return "Цвет: " + response + " alter name: " + alter_name


app = BMW("BMW", "Blue", 4)

print(app.show_color("blacK_color"))
