from colorama import init, Fore, Back, Style
init()
from kahoot import client
from time import sleep
from os import system
import os
import random
import string

bot = client()

def intro():
    os.system('cls')
    print(Fore.LIGHTMAGENTA_EX, """
  | | |  ╦╔═  ╦ ╦  ═╗ ╦
  | | |  ╠╩╗  ╠═╣  ╔╩╦╝
  | | |  ╩ ╩  ╩ ╩  ╩ ╚═                                                                                         
                                                                """)
    print('  | KHX ' + Fore.LIGHTBLACK_EX, 'made by', Fore.LIGHTMAGENTA_EX, 'spxctrzz#0001')
    print(Fore.LIGHTMAGENTA_EX, ' | | https://github.com/spxctrzz')
    print(Fore.LIGHTMAGENTA_EX, ' |')

def bot_game():
    intro()
    random_name_choice = input("  | Random Bot Name? [Y/N] > ")

    if random_name_choice == 'y' or random_name_choice == 'Y':
         bots_name = ''.join((random.choice(string.ascii_lowercase) for num in range(7)))
    else:
         bots_name = input("  | Bots Name > ")

    bots_amount = int(input("  | How Many Bots? > "))
    code = input("  | Kahoot Code > ")
    x = -12
    while x <= bots_amount:
        try:
            bot.join(code, bots_name + " - " + str(x))
            if x >= 0:
                print('    | Sending bots: ' + str(x))
        except:
            print("    |Sorry, Bots Failed.")
            sleep(1)
            beginning()
        finally:
            x += 1
    print(Fore.BLUE, '    | All Bots Successfully Sent ')
    sleep(1)
    beginning()

def ascii_name_spammer():
    intro()
    repeating_word_choice = input("  | Have Name be Repeating Word? [Y/N] > ")
    if repeating_word_choice == 'y' or repeating_word_choice == 'Y':
        bots_name_raw = input("  | Bots Name > ")
        bots_name = (bots_name_raw*100)
    else:
        bots_name = random_ascii_name = ''.join((random.choice(string.ascii_lowercase + string.punctuation + string.digits) for num in range(100)))

    bots_amount = int(input("  | How Many Bots? > "))
    code = input("  | Kahoot Code > ")
    x = -20
    while x <= bots_amount:
        try:
            bot.join(code, bots_name + " - " + str(x))
            if x >= 0:
                print('    | Sending bots: ' + str(x))
        except:
            print("    |Sorry, Bots Failed.")
            sleep(1)
            beginning()
        finally:
            x += 1
    print(Fore.BLUE, '    | All Bots Successfully Sent ')
    sleep(1)
    beginning()



def start():
    menuchoice = input("""  | [1] Flood Game\n  | [2] Long ASCII Name Flooder\n  | >  """)
    if menuchoice == '1':
        bot_game()
    if menuchoice == '2':
        ascii_name_spammer()

def beginning():
    intro()
    start()

beginning()
