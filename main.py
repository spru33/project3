import random
words = ["chair", "money", "rough", "larry", "honey"]
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
def display_word():
    shown = ""
    for letter in secret_word:
        if letter in guessed_letters:
            shown = shown + letter + " "
        else:
            shown = shown + "_ "
    print(shown)
def check_game_status(incorrect_guesses):
    all_guessed = True
    for letter in secret_word:
        if letter not in guessed_letters:
            all_guessed = False
    if all_guessed:
        print("you guessed the word")
        print("final word:")
        display_word()
        return "won"
    if incorrect_guesses >= max_guesses:
        print("you lost, the word was:", secret_word)
        return "lost"
    return "continue"
def play_game():
    incorrect_guesses = 0
    status = "continue"
    while status == "continue":
        print("secret word:")
        display_word()
        print("guessed letters:", guessed_letters)
        print("incorrect guesses remaining:", max_guesses - incorrect_guesses)
        letter = input("enter a letter: ").lower()
        if letter in guessed_letters:
            print("you already guessed that letter")
            continue
        guessed_letters.append(letter)
        if letter not in secret_word:
            incorrect_guesses = incorrect_guesses + 1
            print("incorrect guess")
        else:
            print("correct guess")
        status = check_game_status(incorrect_guesses)
if __name__ == "__main__":
    play_game()