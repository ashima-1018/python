# @classmethod # we can use this method without defining a object as it is a class method.

class PlayerCards:
    membership = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def adding_numbers(cls, num1, num2):
        return num1+num2

    @staticmethod
    # there is no thing called cls they don't care about class attribute
    def adding_numbers2(num1, num2):
        return num1+num2

# we can define like this also as it is class method or we can directly call it by class name as done below

#player1 = PlayerCards('tom', 23)
# print(player1.adding_numbers(2,5))


print(PlayerCards.adding_numbers(2, 3))
