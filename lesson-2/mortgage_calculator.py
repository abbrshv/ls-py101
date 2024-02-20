import json
import math

MONTHS_IN_A_YEAR = 12

with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)


def prompt(message):
    print(f'==> {message}')


def invalid_input(value, last_num=0):
    try:
        float(value)
    except ValueError:
        return True
    return int(value) not in range(1, last_num + 1) if last_num else False


def repeat_input(message, lang='1', last_num=0):
    while True:
        error_msg = MESSAGES[lang][
            'invalid_rng' if last_num else 'invalid_num'].format(last=last_num)

        prompt(message)
        value = input()

        if invalid_input(value, last_num):
            prompt(error_msg)
        else:
            return value


def calculate(lang=''):
    if not lang:
        langs = [f'{key}) {val['language']}' for key, val in MESSAGES.items()]
        lang_msg = MESSAGES['1']['choose_lang'].format(langs=' '.join(langs))
        calculate(repeat_input(lang_msg, '1', len(MESSAGES)))
        return

    messages = MESSAGES[lang]

    amount = float(repeat_input(messages['amount']))
    rate = float(repeat_input(messages['rate'])) / MONTHS_IN_A_YEAR / 100
    duration = math.floor(
        float(repeat_input(messages['duration'])) * MONTHS_IN_A_YEAR)

    monthly_payment = amount * (rate / (
                1 - (1 + rate) ** (-duration))) if rate else amount / duration

    prompt(messages['result'].format(monthly_payment))


calculate()
