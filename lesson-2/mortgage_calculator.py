import json

with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)


def numbers_in_string(string):
    return [int(char) for char in string if char.isdigit()]


def prompt(message):
    print(f'==> {message}')


def invalid_input(value, last_num=0):
    try:
        float(value)
    except ValueError:
        return True
    return int(value) not in range(1, last_num + 1) if last_num else False


def repeat_input(message, lang='en', last_num=0):
    while True:
        error_msg = MESSAGES[lang][
            'invalid_rng' if last_num else 'invalid_num'].format(last=last_num)

        prompt(message)
        value = input()

        if invalid_input(value, last_num):
            prompt(error_msg)
        else:
            return value
