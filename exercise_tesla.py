# also used docstring in this code. It give information what our function is doing
age = input("what is your age?: ")

def checkDriverAge(age=0):  #default value set to 0 
    '''
    this function helps to find whether a person is eligable for driving or not
    '''
    if int(age)<18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age)>18:
        print("Powering On. Enjoy the ride!")
    elif int(age)==18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

# calling a functtion
checkDriverAge()

