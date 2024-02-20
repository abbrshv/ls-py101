import json

with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)


def numbers_in_string(string):
    return [int(char) for char in string if char.isdigit()]


def prompt(message):
    print(f'==> {message}')


def invalid_number(value):
    try:
        float(value)
    except ValueError:
        return True
    return False


def invalid_operation(choice, rng):
    return invalid_number(choice) or not int(choice) in rng


def repeat_input(message, lang='en', rng=range(0)):
    while True:
        prompt(message)
        value = input()

        if rng:
            if invalid_operation(value, rng):
                prompt(
                    MESSAGES[lang]['invalid_operation'].format(last=rng[-1]))
            else:
                return value
        else:
            if invalid_number(value):
                prompt(MESSAGES[lang]['invalid_number'])
            else:
                return value
