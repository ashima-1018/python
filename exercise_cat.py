class Cat:
    speices = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# Find the oldest cat


def oldest_cat(*args):
    return max(args)


# Instantiate the Cat object with 3 cats
cat1 = Cat('Cindy', 10)
cat2 = Cat('tomi', 12)
cat3 = Cat('nana', 11)

# Output
print(
    f'the oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')
