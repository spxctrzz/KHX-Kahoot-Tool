from colorama import init, Fore, Back, Style
init()
from kahoot import client
from time import sleep
import os
import random
import string

bot = client()
updates = 'v1.0, completely new look, profanity filter bypass, and more!

def intro():
    os.system('cls')
    print(Fore.LIGHTMAGENTA_EX, """
  ║ │ ║  ╦╔═  ╦ ╦  ═╗ ╦  ║
  ║ │ ║  ╠╩╗  ╠═╣  ╔╩╦╝  ║
  ║ │ ║  ╩ ╩  ╩ ╩  ╩ ╚═  ║                                                                                       
  ║ │           	               """)
    print('  ║ │ KHX ' + Fore.LIGHTBLACK_EX, 'made by', Fore.LIGHTMAGENTA_EX, 'spxctrzz#0001')
    print(Fore.LIGHTMAGENTA_EX, ' ║ │ https://github.com/spxctrzz')
    print(Fore.LIGHTMAGENTA_EX, ' ║ │ ' + Fore.LIGHTBLACK_EX + updates + Fore.LIGHTMAGENTA_EX)


def bot_game():
    intro()
    random_name_choice = input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Flooder
  ║ Random Bot Name? [Y/N]
  ╚═>>> """)

    if random_name_choice == 'y' or random_name_choice == 'Y':
         bots_name = ''.join((random.choice(string.ascii_lowercase + string.punctuation + string.digits) for num in range(7)))
    else:
         intro()
         bots_name = input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Flooder
  ║ Bots Name
  ╚═>>> """).replace('A', 'А').replace('a', 'а').replace('E', 'Е').replace('e', 'е').replace('I', 'І').replace('i', 'і').replace('O', 'О').replace('o', 'о').replace('C', 'С').replace('c', 'с').replace('Y', 'У').replace('y', 'у')

    intro()
    bots_amount = int(input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Flooder
  ║ Bots Amount
  ╚═>>> """))

    intro()
    code = int(input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Flooder
  ║ Kahoot Code
  ╚═>>> """))
    x = -12
    while x <= bots_amount:
        try:
            bot.join(code, bots_name + " - " + str(x))
            if x >= 0:
                print('    ║ Sending bots: ' + str(x))
        except:
            print("  ║ Sorry, Bots Failed.")
            sleep(1)
            beginning()
        finally:
            x += 1
    print(Fore.BLUE, '  ║ *All Bots Successfully Sent ')
    sleep(1)
    beginning()

def ascii_name_spammer():
    intro()
    repeating_word_choice = input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Long Name Flooder
  ║ Have Name be Repeating Word? [Y/N]
  ╚═>>> """)

    if repeating_word_choice == 'y' or repeating_word_choice == 'Y':
        intro()

        bots_name_raw = input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Long Name Flooder
  ║ Have Name be Repeating Word? 
  ║ >>> """ + repeating_word_choice + """
  ║ Bots Name
  ╚═>>> """).replace('A', 'А').replace('a', 'а').replace('E', 'Е').replace('e', 'е').replace('I', 'І').replace('i', 'і').replace('O', 'О').replace('o', 'о').replace('C', 'С').replace('c', 'с').replace('Y', 'У').replace('y', 'у')

    else:
        bots_name = random_ascii_name = ''.join((random.choice(string.ascii_lowercase + string.punctuation + string.digits) for num in range(100)))

    intro()

    bots_amount = int(input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Long Name Flooder
  ║ Have Name be Repeating Word? 
  ║ >>> """ + repeating_word_choice + """
  ║ Bots Name
  ║ >>> """ + bots_name + """
  ╚═>>> """))
    intro()
    code = input("""
  ╔═══════════════════════════════════════════════
  ║ >>> Long Name Flooder
  ║ Have Name be Repeating Word? 
  ║ >>> """ + repeating_word_choice + """
  ║ Bots Name
  ║ >>> """ + bots_name + """
  ║ Kahoot Code
  ╚═>>> """)
    x = -20
    while x <= int(bots_amount):
        try:
            bot.join(code, bots_name + " - " + str(x))
            if x >= 0:
                print('    │ Sending bots: ' + str(x))
        except:
            print("    │ Sorry, Bots Failed.")
            sleep(1)
            beginning()
        finally:
            x += 1
    print(Fore.BLUE, '    │ All Bots Successfully Sent ')
    sleep(1)
    beginning()

def start():
    menuchoice = input("""
  ╔═══════════════════════════════════════════════
  ║ [1] Flood Game
  ║ [2] Long ASCII Name Flooder  
  ╚═>>> """)

    if menuchoice == '1':
        bot_game()
    if menuchoice == '2':
        ascii_name_spammer()

def beginning():
    intro()
    start()

beginning()
