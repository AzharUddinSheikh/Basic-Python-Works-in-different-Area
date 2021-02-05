import random
import string

# provide floating point number
(random.random())

# randomly pick number between provided int
y = random.randint(1, 10)
# print(y)

# randomly pick number of choice
y = random.choice([1, 32, 5, 6])
# print(y)

# multiple randomly picked
y = random.choices([1, 2, 34, 5], k=2)
# print(y)

# for randomly pass
y = (",".join(random.choices("azharuddin", k=5)))
# print(y)


y = ("".join(random.choices(string.ascii_letters+string.digits, k=5)))
# print(y)

# print(string.ascii_letters)
# print(string.digits)

# shuffling the random number
number = [1, 2, 3, 5]
random.shuffle(number)
print(number)
