# Truthy and Falsly
#All the valsues in python is truthy expect empty list, set , dict, 0 None anything which is zero is a falsy value.
 

# Ternanry Operator
## condition-if-true if condition else condition-if-false
is_friend = False
can_message =  "message allowed" if is_friend else "not allowed to message"
print("message")


# Short Circuiting 
and / or these are the short ciricuting one 
if any one of the condition is true or false they are not checking the other condition so that is called short circuiting

# IS or == difference 
== checks for the equality of the items whereas IS checks for the same memory location 


# Dict 
for key, value in dictonary:
    print (key,value)

for item in dictonary.keys():
    print (item)

for item in dictonary.items():
    print (item)

for item in dictonary.values():
    print (item)


# Enumerate()
In this we will get index and char both 
for index, char in enumerate([1,2,3,4,5,6]):
    print(index,char)     --->>> it will give 0 1 1 2 2 3 ........
    
