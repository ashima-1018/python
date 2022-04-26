# *args && **kwargs

def super_func(*args):
    print(args)
    return sum(args)

super_func(1,2,3,4,5)  # it will give error as there we give 5 arguments in the function

# to solve this we need to have *args

def super_funcc(*args):
    print(*args)
    return sum(args)

print(super_funcc(1,2,3,4,5)) # this will give us the output 15 actually. and if use print(args) it will print as a tuple (1,2,3,4,5)


# **kwargs
# it will take keyword argumentS and retrun the dictonary as a output

def super_funccc(*args, **kwargs):     # as **kwargs will return output as dictonary so we need to reterive the value as we do in dictonary
    total = 0 
    for items in kwargs.values():
        total += items
    return sum(args)+total 
 
print(super_funccc(1,2,3,4,5, num1=5, num2 =10))



# there is a rule for pramameters to follow :
# params, *args, default parameters, **kwargs

