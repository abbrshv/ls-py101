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


def validate_input(message, lang='1', last_num=0):
    while True:
        error_msg = MESSAGES[lang][
            'invalid_rng' if last_num else 'invalid_num'].format(last=last_num)

        prompt(message)
        value = input()

        if invalid_input(value, last_num):
            prompt(error_msg)
        else:
            return value if last_num else float(value)


def choose_language():
    langs = [f'{key}) {val['language']}' for key, val in MESSAGES.items()]
    lang_msg = MESSAGES['1']['choose_lang'].format(langs=' '.join(langs))
    return validate_input(lang_msg, '1', len(MESSAGES))


def calc_monthly_payment(messages):
    amount = validate_input(messages['amount'])
    rate = validate_input(messages['rate']) / MONTHS_IN_A_YEAR / 100
    duration = math.floor(
        validate_input(messages['duration'])) * MONTHS_IN_A_YEAR

    return amount * (rate / (
            1 - (1 + rate) ** (-duration))) if rate else amount / duration


def calculator(lang=''):
    if not lang:
        calculator(choose_language())
        return

    messages = MESSAGES[lang]
    prompt(messages['welcome'])
    prompt(messages['result'].format(calc_monthly_payment(messages)))

    if validate_input(messages['again'], lang, 2) == '1':
        calculator(lang)


calculator()
