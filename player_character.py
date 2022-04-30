class PlayerCharacter:  # initalsie class which is known as blueprint

    membership = True  # class object attribute it is static as it is true for every object that is initalize from this class

    def __init__(self, name, age):   # this is a constructor
        if (PlayerCharacter.membership):    # or we can use self.membership also
            self.name = name  # dynamic attributes
            self.age = age

    def run(self):   # this is a method and it will return None if we add return as done it will return done
        print(f'my name is {self.name}')
        # return 'done'


player1 = PlayerCharacter('Cindy', 23)  # initiantise a object from the class
player2 = PlayerCharacter('Tom', 35)

print(player1.name)
print(player1.run())
print(player2.age)
