import random

def print_hangman(tries):
    stages = [
        """
        ------
        |    |
        |
        |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |    |
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   /
        |
        -
        """,
        """
        ------
        |    |
        |    O
        |   /|\\
        |   / \\
        |
        -
        """,
    ]
    return stages[tries]

def main():
    print("Welcome to the Hangman game!")
    words = ["python", "java", "javascript", "ruby", "php", "csharp", "swift"]
    secret_word = random.choice(words)
    guessed_word = "-" * len(secret_word)
    tries = 6
    guessed_letters = []

    while guessed_word != secret_word and tries >= 0:
        print("\n" + guessed_word)
        print(print_hangman(6 - tries))
        letter = input("Enter a letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Please enter a single letter.")
            continue

        if letter in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(letter)

        if letter in secret_word:
            new_guessed_word = ""
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    new_guessed_word += letter
                else:
                    new_guessed_word += guessed_word[i]
            guessed_word = new_guessed_word
        else:
            print("Wrong guess!")
            tries -= 1

    if guessed_word == secret_word:
        print("\nCongratulations! You guessed the word:", secret_word)
    else:
        print("\nSorry, you're out of tries. The word was:", secret_word)

if __name__ == "__main__":
    main()
