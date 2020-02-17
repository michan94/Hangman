import random;

#Setting up the game
import string

words = ["awkward", "bagpipes", "crypt", "decline", "tank", "python", "aeiou"];
wordToGuess = random.choice(words);

def hangman(wordToGuess):
    print(wordToGuess);
    numGuessesLeft = 3;
    guessedLetters = [];
    correctGuesses = [];

    for correctletter in wordToGuess:
        correctGuesses.append(correctletter);

    print("Your word contains " + str(len(wordToGuess)) + " letters");

    output = ["_"] * len(wordToGuess);
    print(output)
    #print(' '.join(c if c in guessedLetters else "_" for c in wordToGuess));

    print("Guess a letter wrong and you lose a guess");

    while (numGuessesLeft > 0 and len(correctGuesses) != 0):
        guess = input("Guess a letter: ");
        guess = guess.lower();
        print(guess);
        if guess not in guessedLetters:
            guessedLetters.append(guess);
            if guess in wordToGuess:
                correctGuesses.remove(guess);
                # for i, x in enumerate(wordToGuess):
                #     if x is guess:
                #         output[i] = guess;

            else:
                numGuessesLeft -= 1;
                if numGuessesLeft == 0:
                    print("You are out of guesses. Thanks for playing");
                    break;
                else:
                    print("Sorry, guess again");
                #numGuessesLeft -= 1;
        elif guess in guessedLetters:
            print("Letter already guessed. Make another guess")
            continue;
    if len(correctGuesses) == 0:
        print("Congratulations! You've won!")



#Start the game
response = input("Welcome to Hangman. Are you ready to play? (y/n)\n");
response.lower();
if response == "y":
    print("Let's Start!");
    hangman(wordToGuess);
elif response == "n":
    print("Thanks for playing");


