import random
import time


player_name = input("Please tell me your name :")
class player:
    def __init__(self, player_name ):
        self.player_name  = player_name

    def print(self):
        print(f'Welcome to the Dice Game {self.player_name}......')
        time.sleep(2)
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
        else:
            print("Whether you choose Y or N, you have no choice. Accept your fate.")
        time.sleep(3)
        print("Prepare yourself for a test of fate, where the roll of a dice will determine your destiny.")
        time.sleep(3)
        print("In this game, you'll face off against the computer in a battle of luck and strategy.")
        time.sleep(3)
        print("But remember, only one will emerge victorious.")
        time.sleep(3)
        choice2 = input("Are you willing to take the risk and roll the dice? (Y/N): ")
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


player1 = player(player_name)
player1.print()