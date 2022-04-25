from gallows import Gallows
from gallows_game_status import GameStatus


def chars_list_to_str(chars):
    return ''.join(chars)


game = Gallows()
word = game.generate_word()

letters_count = len(word)

print(f'The word consists of {letters_count} letters.')
print('Try to guess the word letter by letter.')

while game.game_status == GameStatus.IN_PROGRESS:
    letter = input('Pick a letter.\n')
    state = game.guess_letter(letter)

    print(chars_list_to_str(state))

    print(f'Remaining tries = {game.remaining_rtries}')
    print(f'Tried letter: {chars_list_to_str(game.tried_letters)}')

if game.game_status == GameStatus.LOST:
    print("You're hanged!")
    print(f'The word was: {game.word}')
else:
    print('Congratulations! You won!')
