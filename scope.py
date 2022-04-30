# scope
# what variables do I have access to?

# scope in a function
# if we are creating a variable inside a function the scope of that variable is only in that function.

from re import X


a = 1   # global variable


def parent():    # checking for parent varibale example
    a = 10

    def confusion():
        return a     # funtional variable (it's own world)
    return confusion()


print(a)  # --> 1
print(confusion())  # --> 5


# Order Rules
# Rule 1 --> checks for local variable
# rule 2 --> parent local it checks
# rule 3 --> global variables
# rule 4 --> built in python functions


# parameters are defined as a local variable as we are giving them as the parameter to a function
def confusion(b):
    print(b)


confusion(300)   # output 300 as it is loal function varibale example


# how to access global varibale in a function example
total = 0


def count():
    global total
    total += 1
    return total


count()
count()
print(count())       # this whole give us the output as 3


# nonlocal varibale new in python 3 example
def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner', x)
    inner()
    print("outer", x)


outer()
