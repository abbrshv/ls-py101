import os

VALID_CHOICES = ('rock', 'paper', 'scissors')
VALID_CHOICES_EXT = VALID_CHOICES + ('spock', 'lizard')


def prompt(message):
    print(f'==> {message}')


def get_player_choice(valid_choices):
    while True:
        prompt(f'Choose one: {', '.join(valid_choices)}')
        prompt(
            f'You can write a either a full word, e.g: "{valid_choices[0]}",'
            f' or a short version, e.g: '
            f'"{valid_choices[0][0]}", "{valid_choices[0][0:2]}"')

        choice = input().strip().lower()
        choices_left = [option for option in valid_choices if choice in option]

        os.system('clear')

        match len(choices_left):
            case 0:
                prompt('That\'s not a valid choice\n')
            case 1:
                break
            case _:
                prompt(
                    f'You probably meant one of: {", ".join(choices_left)}?\n'
                    f'Adding one more letter might make it easier to guess '
                    f'your intentions\n')

    return valid_choices.index(choices_left[0])
