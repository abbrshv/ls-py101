import os

MODES = {'basic rps': ('rock', 'paper', 'scissors'),
         'spock lizard': ('rock', 'paper', 'scissors', 'spock', 'lizard'), }


def prompt(message):
    print(f'==> {message}')


def get_player_choice(valid_choices):
    prompt(f'Choose one: {', '.join(valid_choices)}')
    prompt(f'You can write a either a full word, e.g: "{valid_choices[0]}",'
           f' or first letter(s) only, e.g: '
           f'"{valid_choices[0][0]}", "{valid_choices[0][0:2]}"')

    choice = input().strip().lower()
    matches = [option for option in valid_choices if option.startswith(choice)]

    os.system('cls||clear')

    match len(matches):
        case 0:
            prompt('That\'s not a valid choice\n')
        case 1:
            return matches[0]
        case _:
            prompt(f'You probably meant one of: {", ".join(matches)}?\n'
                   f'Adding one more letter might make it easier to guess '
                   f'your intentions\n')

    return get_player_choice(valid_choices)


def get_round_result(player_choice, computer_choice):
    round_result = player_choice - computer_choice

    is_tie = round_result == 0
    is_win = round_result % 2 == 0 if round_result < 0 \
        else round_result % 2 != 0

    if is_tie:
        return []
    return {'player': int(is_win), 'computer': int(not is_win)}
