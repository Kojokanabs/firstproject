import random
import Logo_art
EASY_LEVEL_TRY = 10 #If you want a variable to be constant...capital letter
HARD_LEVEL_TRY = 5
def level_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_TRY
    elif level_chosen == "hard":
        return HARD_LEVEL_TRY
    else:
        return

def check_answer (guessed_number, system_choice, attempts_try) :
    if guessed_number < system_choice:
        print("Your guess is too low")
        return attempts_try - 1
    elif guessed_number > system_choice:
        print("Your guess is too high")
        return attempts_try - 1
    else:
        print(f"Your guess was right...The answer was {system_choice}")

def game ():
    print(Logo_art.design)
    print("Let me think of a number between 1 to 50:")
    system_choice = random.randint(1,50)
    #print(system_choice) i dont want the guessed number to be showned
    choice = input("Choose level of difficulty... Type 'easy' or 'hard': ")
    attempts_try = level_difficulty(choice)
    if attempts_try != EASY_LEVEL_TRY and attempts_try != HARD_LEVEL_TRY:
        print("You have entered a wrong difficulty level...Play again!!")
        return

    guessed_number = 0
    while guessed_number != system_choice:
        print(f"You have {attempts_try} remaining to guess the number. ")
        guessed_number = int(input("Guess a number: "))
        attempts_try = check_answer(guessed_number, system_choice, attempts_try)
        if attempts_try == 0:
            print("You are out of guesses...You lose!")
            return
        elif guessed_number != system_choice:
            print("Guess again")
game()