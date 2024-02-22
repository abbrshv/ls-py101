import os
from random import randrange

MODES = {'Basic': ('Rock', 'Paper', 'Scissors'),
         'Spock Lizard Expansion': (
             'Rock', 'Paper', 'Scissors', 'Spock', 'Lizard'), }
WIN_ROUNDS = 3


def prompt(message):
    print(f'==> {message}')


def get_player_choice(valid_choices):
    if any(len(val) > 1 for val in valid_choices):
        prompt(f'Choose one: {', '.join(valid_choices)}')
        prompt(f'You can write either a full word, e.g: "{valid_choices[0]}",'
               f' or first letter(s) only, e.g: '
               f'"{valid_choices[0][0]}", "{valid_choices[0][0:2].lower()}"')

    choice = input().strip().lower()
    matches = [val for val in valid_choices if val.lower().startswith(choice)]

    os.system('cls||clear')  # Should clear console for both Win and macOS/Unix

    match len(matches):
        case 0:
            prompt('That\'s not a valid choice\n\n')
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
        return None
    return is_win


def play_game():
    prompt('Hello there! Welcome to Rock Paper Scissors')
    prompt('What kind of Rock Paper Scissors would you like to play?\n')

    game_mode = get_player_choice(list(MODES.keys()))
    valid_choices = MODES[game_mode]
    prompt(f'Let the game of {', '.join(valid_choices[:-1])} '
           f'and {valid_choices[-1]} begin!\n\n')

    score = {'player': 0, 'computer': 0}
    while score['player'] < WIN_ROUNDS and score['computer'] < WIN_ROUNDS:
        player_choice = get_player_choice(valid_choices)
        computer_choice = randrange(len(valid_choices))
        prompt(f'You chose {player_choice}, '
               f'computer chose {valid_choices[computer_choice]}')

        round_result = get_round_result(valid_choices.index(player_choice),
                                        computer_choice)
        if round_result is not None:
            score['player' if round_result else 'computer'] += 1

        prompt(f'You: {score['player']}  Computer: {score['computer']}\n')

    player_won = score['player'] == WIN_ROUNDS
    prompt(f'Game Over, {'You' if player_won else 'Computer'} won. '
           f'{'Congratulations' if player_won else 'Good luck next time'}!')


play_game()
