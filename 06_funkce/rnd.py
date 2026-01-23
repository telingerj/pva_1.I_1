import random
x = [1, 2, 3, 4, 5, 6]

print(random.random() + random.randint(1, 5))
random.shuffle(x)
print(x)