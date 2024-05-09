import random
import time

player_name= ""
def intro():
    print("Welcome to the Dice Game......")
    time.sleep(2)
    player_name = input("Please tell me your name :"  )
    print("......")
    time.sleep(1)
    print(f'{player_name}, you may not know me, but I know what you did.')
    time.sleep(2)
    choice = input("Do you dare to play a game of chance? Y/N: ")
    time.sleep(1)
    print("You've chosen: ", choice)
    time.sleep(2)
    if choice.upper() == "Y":
        print("Very good....")
    else :
        print("Whether you choose Y or N, you have no choice. Accept your fate.")
    time.sleep(3)
    print("Prepare yourself for a test of fate, where the roll of a dice will determine your destiny.")
    time.sleep(3)
    print("In this game, you'll face off against the computer in a battle of luck and strategy." )
    time.sleep(3)
    print("But remember, only one will emerge victorious.")
    time.sleep(3)
    choice2= input("Are you willing to take the risk and roll the dice? (Y/N): ")
    time.sleep(1)
    print("......")
    time.sleep(1)
    print("You've chosen: ", choice2)
    time.sleep(3)
    print("Again, Whether you choose Y or N, you have no choice. you must play the game.")
    time.sleep(1)
    print("    ")
    time.sleep(1)
    print("    ")
    time.sleep(1)
    print("    ")
    time.sleep(1)
    print("Let's begin the game.")

def random_num():
    return random.randint(1, 6)

def dice_game():
    intro()
    computer = []
    player1 = []

    while True:
        input("Press enter when you are ready... ")
        number = random.randint(1, 6)
        time.sleep(2)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Your dice is:", number)
        time.sleep(2)
        print("saving.....")
        time.sleep(2)
        print("   ")
        time.sleep(2)
        player1.append(number)
        print(f"Your score: {number} has been saved in your inventory.")
        time.sleep(2)
        print(f'Current score'
              f' You : {sum(player1)} Computer: {sum(computer)}')
        time.sleep(2)

        if sum(player1) >= 10 or sum(computer) >= 10:
            break

        print("Computer is playing the game...")
        c_number = random.randint(1, 6)
        time.sleep(2)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Computer's dice is:", c_number)
        time.sleep(2)
        print("saving.....")
        time.sleep(2)
        print("   ")
        time.sleep(2)
        computer.append(c_number)
        print(f"Computer score: {c_number} has been saved in its inventory.")
        time.sleep(2)
        print(f'Current score '
              f'You: {sum(player1)} Computer: {sum(computer)}')
        time.sleep(2)

        if sum(player1) >= 10 or sum(computer) >= 10:
            break

    if sum(player1) >= 10 and sum(computer) < 10:
        print("Game is over")
        time.sleep(2)
        print("Congratulations You win")
    elif sum(computer) >= 10 and sum(player1) < 10:
        print("Game is over")
        time.sleep(2)
        print("I win the game....")
    else:
        print("It's a tie")
        time.sleep(2)

    time.sleep(3)
    print("Listen....")
    time.sleep(2)
    print("Just like rolling dice, life is unpredictable, filled with unexpected twists and turns.")
    time.sleep(3)
    print(
        "If your initial belief in 'if there is a will, there is a way' remains unchanged, you will be able to accomplish anything.")
    time.sleep(3)
    print("Run towards the exit without looking back.")
    time.sleep(2)
    print("Exit game")
    time.sleep(2)
    print("**End**")

dice_game()
