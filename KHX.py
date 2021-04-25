from colorama import init, Fore, Back, Style
init()
from kahoot import *
from time import sleep
import keyboard
from os import system
import os
import random
import string

bot = client()

def intro():
    print(Fore.LIGHTMAGENTA_EX, """
  | | |  ╦╔═  ╦ ╦  ═╗ ╦
  | | |  ╠╩╗  ╠═╣  ╔╩╦╝
  | | |  ╩ ╩  ╩ ╩  ╩ ╚═                                                                                         
                                                                """)
    print('  | KHX ' + Fore.LIGHTBLACK_EX, 'made by', Fore.LIGHTMAGENTA_EX, 'spxctrzz#0001')
    print(Fore.LIGHTMAGENTA_EX, ' | | https://github.com/spxctrzz')
    print(Fore.LIGHTMAGENTA_EX, ' |')

def bot_game():
    os.system('cls')
    intro()
    random_name_choice = input("  | Random Bot Name? [Y/N] > ")

    if random_name_choice == 'y':
        bots_name = ''.join((random.choice(string.ascii_lowercase) for num in range(11)))
    else:
        bots_name = input("  | Bots Name > ")

    bots_amount = int(input("  | How Many Bots? > "))
    code = input("  | Kahoot Code > ")
    x = 0
    while x <= bots_amount:
        try:
            bot.join(code, bots_name + " - " + str(x))
            print('    | Sending bots: ' + str(x))
        except:
            print("    |Sorry, Bots Failed.")
            sleep(1)
            os.system('cls')
            beginning()
        finally:
            x += 1
    print(Fore.BLUE, '    | All Bots Successfully Sent ')
    sleep(1)
    beginning()


def start():
    menuchoice = input("  | [1] Flood Game\n  |\n  | > ")
    if menuchoice == '1':
        bot_game()


def beginning():
    intro()
    start()

beginning()