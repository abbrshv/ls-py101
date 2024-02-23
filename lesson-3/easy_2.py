# pylint: skip-file

# Question 1
numbers = [1, 2, 3, 4, 5]

print(list(reversed(numbers)))
print(numbers[::-1])

# Question 2
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False
number2 = 95  # True

print(number1 in numbers)
print(number2 in numbers)

# Question 3
rng = range(10, 101)

print(42 in rng)
print(100 in rng)
print(101 in rng)

# Question 4
numbers = [1, 2, 3, 4, 5]

numbers.pop(2)
print(numbers)

# Question 5
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers) is list)
print(type(table) is list)
print(isinstance(numbers, list))
print(isinstance(table, list))

# Question 6
title = "Flintstone Family Members"

just_title = title.center(40)
print(repr(just_title))

# Question 7
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))

# Question 8
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('Spot' in ages)

# Question 9
ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}
additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)
print(ages)
