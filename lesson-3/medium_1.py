# Question 1
def flintsones_rock():
    for i in range(10):
        print(' ' * i + 'The Flintstones Rock!')


flintsones_rock()


# Question 2
def factors(number):
    divisor = number
    result = []
    while divisor != 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1 if number > 0 else -1
    return result if number > 0 else result + [-n for n in result]


print(factors(-6))
