import random

random_digits = []
numbers = int(input("Enter the number of digits: "))
random_string = ''

for _ in range(numbers):
    number = random.randint(0, 9)
    random_digits.append(number)

for digit in random_digits:
    random_string += str(digit)

print(random_string)
