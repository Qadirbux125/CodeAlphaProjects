import random

def choose_word():
    #list of words for the game
    words = ['python','hangman','programmig','developer','computer','codealpha']
    return random.choice(words)

def display_word(word,guessed_letters):
    #display the word with blanks for unguessed  latters
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6 # limit of incorrect guesses

    print("Welcome to hangman!")

    while incorrect_guesses<max_incorrect_guesses:
        print(f"Word:{display_word(word,guessed_letters)}")
        print(f"Incorrect guesses left:{max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        #check if input is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        #Check if the letter  has already been guessed
        if guess in guessed_letters:
            print("you already that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess!'{guess}'is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops!'{guess}'is not in the word.")

        #check if player has guessed all the letters
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was:{word}")


#start the game
hangman()