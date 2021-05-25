import random
from hangman_art import logo, stages
import hangman_words 


game_over = False
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
lives = 6

print(logo)
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += '_'

while not game_over:
    guess = input("Guess a letter: ").lower()
    if guess in display:
          print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, thats not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose")
    print(f"{' '.join(display)}")

    if '_' not in display and lives > 0:
        game_over = True
        print("You Win")

    print(stages[lives])