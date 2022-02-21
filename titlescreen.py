#title screen test
import cmd
import sys
import os
import time
import random
import textwrap

os.system('mode con: cols=190 lines=45')

def typing(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
        
def ftyping(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.04)
        
def styping(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
        
def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')
        
def start():
    clrscrn()
    time.sleep(3)        
    ftyping ("Welcome to our first little game\n\n\n\n\nCreated by;\n")
    time.sleep(1)
    print ( '''
     :::    ::: :::::::::: :::::::::: ::::::::  :::    ::: :::   :::           :::     ::::    ::: :::::::::         ::::::::  ::::    ::: ::::::::::     :::     :::    ::: :::   ::: 
     :+:   :+:  :+:        :+:       :+:    :+: :+:    :+: :+:   :+:         :+: :+:   :+:+:   :+: :+:    :+:       :+:    :+: :+:+:   :+: :+:          :+: :+:   :+:   :+:  :+:   :+: 
     +:+  +:+   +:+        +:+       +:+        +:+    +:+  +:+ +:+         +:+   +:+  :+:+:+  +:+ +:+    +:+       +:+        :+:+:+  +:+ +:+         +:+   +:+  +:+  +:+    +:+ +:+  
     +#++:++    +#++:++#   +#++:++#  +#+        +#++:++#++   +#++:         +#++:++#++: +#+ +:+ +#+ +#+    +:+       +#++:++#++ +#+ +:+ +#+ +#++:++#   +#++:++#++: +#++:++      +#++:   
     +#+  +#+   +#+        +#+       +#+        +#+    +#+    +#+          +#+     +#+ +#+  +#+#+# +#+    +#+              +#+ +#+  +#+#+# +#+        +#+     +#+ +#+  +#+      +#+    
     #+#   #+#  #+#        #+#       #+#    #+# #+#    #+#    #+#          #+#     #+# #+#   #+#+# #+#    #+#       #+#    #+# #+#   #+#+# #+#        #+#     #+# #+#   #+#     #+#    
     ###    ### ########## ########## ########  ###    ###    ###          ###     ### ###    #### #########         ########  ###    #### ########## ###     ### ###    ###    ###    ''')            
    time.sleep(5)
    clrscrn()
    styping ("In this game you will encounter random events against random enemies, everytime you play this game it will play differently.\n\n\n\n\n")
    input ("Press Enter to Begin")
    clrscrn()
    from Prologue import Prologue #imorting Prologue into this #bring Prologue to the game
    
    Prologue()

def title_screen_select():
    option = input()
    while 0 == 0 and option != 0:
        if option == ("play") or option ==  ("Play"):
                start()
        elif option == ("Credits") or option ==  ("credits"):
                credits()
        elif option == ("Exit")or option == ("exit"):
                sys.exit()
        elif option != ("Play") or option != ("play") or option != ("Credits") or option !=  ("credits") or option != ("Exit") or option != ("exit"):
                typing ("please input valid command\n")
                option = 0
                option = input()
    
    
    
def title_screen():
    print ("")
    print("")
    print(" ")
    print("                                                  ###############################################################################################")
    print("                                                                                             Play")
    print("                                                                                           Credits")
    print("                                                                                             Exit")
    print("                                                  ###############################################################################################")
    title_screen_select()
    
def deathseq():
    if (char['HP'] <= 0):
        print ("You have been slain")
        time.sleep(4)
        endscr()


def endscr():
    clrscrn()
    
    
    redo = input ("Thank you for playing our game, If you would like to play again Press 1, Press 2 to exit\n")
    if redo == ("1"):
        start()
    elif redo == ("2"):
        os.system(exit)
    
def credits():
    clrscrn()
    print ("Thank you for playing our game, this is our first attempt and we have no prior coding experience.\nA lot of help was gathered from github, youtube, x3 and stackoverflow.\n")
    print ("Made by Tomas Keech and Jason Mutter\n\n\n\n\n")
    input ("Press Enter to return to Title Screen")
    clrscrn()
    title_screen()

title_screen()
