import os
from random import randrange

RPS = {
    'Basic': {'choices': ('Rock', 'Paper', 'Scissors')},
    'Spock Lizard Expansion': {
        'choices': ('Rock', 'Paper', 'Scissors', 'Spock', 'Lizard'),
        'rules': '''Scissors cuts Paper covers Rock crushes Lizard poisons 
Spock smashes Scissors decapitates Lizard eats 
Paper disproves Spock vaporizes Rock crushes Scissors'''
    },
}
WIN_ROUNDS = 3


def prompt(message):
    print(f'==> {message}')


def clear_terminal():
    os.system('cls||clear')  # Should clear console for both Win and macOS/Unix


def get_player_choice(valid_choices):
    prompt(f'Choose one: {', '.join(valid_choices)}')
    if any(len(val) > 1 for val in valid_choices):
        prompt(f'You can write either a full word, e.g. "{valid_choices[0]}",'
               f' or first letter(s) only, e.g. '
               f'"{valid_choices[0][0]}", "{valid_choices[1][0:2].lower()}"')

    choice = input().strip().lower()
    matches = [val for val in valid_choices if val.lower().startswith(choice)]

    clear_terminal()

    if len(matches) == 1:
        return matches[0]
    if matches:
        prompt(f'You probably meant one of: {", ".join(matches)}?\n'
               f'Using two letters, e.g. "{matches[0][0:2].lower()}" '
               f'might clarify that\n')
    else:
        prompt('That\'s not a valid choice\n\n')

    return get_player_choice(valid_choices)


def determine_winner(player_choice, computer_choice):
    round_result = player_choice - computer_choice

    is_tie = round_result == 0
    is_win = round_result % 2 == 0 if round_result < 0 \
        else round_result % 2 != 0

    if is_tie:
        return None
    return is_win


def play_round(valid_choices):
    player_choice = get_player_choice(valid_choices)
    computer_choice_idx = randrange(len(valid_choices))
    prompt(f'You chose {player_choice}, '
           f'computer chose {valid_choices[computer_choice_idx]}')

    return determine_winner(valid_choices.index(player_choice),
                            computer_choice_idx)


def display_rules(game_mode):
    prompt('Would you like to see the rules? y/n')
    if get_player_choice(['y', 'n']) == 'y':
        clear_terminal()
        print(RPS[game_mode]['rules'] + '\n')
        prompt('Press Enter to begin the game')
        input()
        clear_terminal()


def play_game(game_mode=''):
    if not game_mode:
        prompt('Hello there! Welcome to Rock Paper Scissors!')
        prompt('What kind of Rock Paper Scissors would you like to play?\n')
        game_mode = get_player_choice(list(RPS.keys()))
        play_game(game_mode)
        return

    if game_mode != 'Basic':
        display_rules(game_mode)

    valid_choices = RPS[game_mode]['choices']
    prompt(f'Let the game of {', '.join(valid_choices[:-1])} '
           f'and {valid_choices[-1]} begin!\n\n')

    score = {'player': 0, 'computer': 0}
    while score['player'] < WIN_ROUNDS and score['computer'] < WIN_ROUNDS:
        round_result = play_round(valid_choices)

        if round_result is not None:
            score['player' if round_result else 'computer'] += 1

        prompt(f'You: {score['player']}  Computer: {score['computer']}\n')

    player_won = score['player'] == WIN_ROUNDS
    prompt(f'Game Over, {'You' if player_won else 'Computer'} won. '
           f'{'Congratulations' if player_won else 'Good luck next time'}! '
           'Care for another game? y/n')

    if get_player_choice(['y', 'n']) == 'y':
        play_game(game_mode)
    else:
        prompt('Goodbye, see you soon!')


play_game()
