from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print("Too high🙄")
        return turns - 1
    elif guess < answer:
        print("Too low🙃")
        return turns - 1
    else:
        print("You got it!😍")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def play_game():
    print("Welcome to the Number Guessing game😉\nI'm thinking of a number between 1 and 100🤔")
    answer = randint(1, 101)
    
    turns = set_difficulty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The right number was: '{answer}' ")
            return
        elif guess != answer:
            print("Guess again😉")

while input("Do you want to play 'Number Guessing game'?🥰 Type 'y' or 'n': ") == "y":
    play_game()