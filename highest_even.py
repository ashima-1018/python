def highest_even(li):
    even =[]
    for items in li:
        if items %2 ==0:
            even.append(items)
    return max(even)

print(highest_even([2,10,2,3,4,8,11]))