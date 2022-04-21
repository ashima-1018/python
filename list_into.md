This is the introduction to list

intro_list = ['hey',2,3,4,True]
print(intro_list[0])
same as array 
they are mutable
Comapre to strings as strings are immutable 

#######List Slicing #########

If you need to copy the list then you need to copy the list in the slicing way. 
eg 
new_list = old_list[:]

else
new_list = old_list  this will modify the actual list also if we do this way.

# List Methods
all the list methods are in place methods they don't produce any output they just add or remove the list in place.
eg 
basket = [1,2,3,4,5]
basket.pop()  --> by default last element will be popped out or else you can give index number specificaaly if you want.
basket.append([100])
basket.extend([1001,1002])
basket.remove(2) --> here we need to give value what we need to remove from the list nor index

if we do 
new_basket =  basket.append([100])
print(basket) --> It will give us NONE as the output. 
as it will not assign anything only modify the list but don't assign it to the other list or new list.
If we want to copy the list to new list we need to do the following
basket.append([100])
new_list = basket

# List unpacking 

a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
print(a)   --> output 1
print(b)   --> output 2
print(c)   --> output 3
print(other)   --> output [4,5,6,7,8]
print(d)   --> output 9