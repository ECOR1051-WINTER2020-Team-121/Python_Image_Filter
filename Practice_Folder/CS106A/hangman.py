from random_word import RandomWords


def menu() -> None:
    """
    RETURNS None.
    Is the menu interface. Gives user option
    to play or to quit.

    >>> menu()
    """
    is_exit = False

    while not is_exit:
        print("Would you like to play hangman? [Y/N]\n")
        response = input("Choice: ").lower()
        if response == 'y':
            play_hangman()
        elif response == 'n':
            is_exit = True
        else:
            print("Invalid response.")


def play_hangman() -> None:
    """
    RETURNS None.
    Controls the game interface.

    >>> play_hangman()
    """
    num_guesses = 10
    guessed_letters = set()
    r = RandomWords()
    word = str(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech='noun', maxLength=5))

    print("Welcome to Hangman.\n")

    while num_guesses > 0:
        print("The word now looks like this: {}".format(format_word(word, guessed_letters)))
        display_num_guesses(num_guesses)


def format_word(word: str, guessed_letters: set) -> str:
    """
    RETURNS a str. A string of
    dashes is modified to reveal
    certain letters, based on
    guessed_letters

    >>> format_word('hello', {'e', 'l'})
    '-ell-'
    """
    hidden_word = '-' * len(word)

    for letter in guessed_letters:
        if letter in word:





