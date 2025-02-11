import random

def hangman():
    words = ["python", "hangman", "programming", "code", "computer"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    
    while attempts > 0:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word:", display_word)
        
        if "_" not in display_word:
            print("Congratulations! You guessed the word.")
            break

        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.append(guess)
            print("Good job! Keep going.")
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

    if attempts == 0:
        print(f"Game Over! The word was: {word}")

hangman()
