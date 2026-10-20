
import random

def play_hangman():
    words = ["python", "computer", "program", "developer", "coding"]
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("\n================================")
    print("       WELCOME TO HANGMAN")
    print("================================")
    print("Guess the hidden word one letter at a time!")
    print("You have 6 incorrect guesses available.\n")

    while incorrect_guesses < max_attempts:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Incorrect guesses:", incorrect_guesses, "/", max_attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You guessed the word:", secret_word)
            print("You win!")
            break

        guess = input("\nEnter a single letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another!\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

    else:
        print("\nGame over! You used all 6 incorrect guesses.")
        print("The correct word was:", secret_word)

    print("\nThanks for playing Hangman!")


if __name__ == "__main__":
    play_hangman()
