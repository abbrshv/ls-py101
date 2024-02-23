# pylint: skip-file

# Question 1
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)

numbers = [1, 2, 3, 4]
while numbers:
    numbers.pop()
print(numbers)


# Question 5
def is_color_valid(color):
    # if color == "blue" or color == "green":
    #     return True
    # else:
    #     return False

    # return color == "blue" or color == "green"
    return color in ["blue", "green"]
