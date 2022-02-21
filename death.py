import time
import cmd
import os
import random
import textwrap
import sys

char = {'lvl': 1,
        'xp' : 0,
        'lvlnext' : 10,
        'ATK': 10,
         'DEF': 5,
         'HP' : 10}

def level(char,): #Level system for the hero
       while char['xp'] >= char['lvlnext']: #if xp is greater to or equal to lvlnext xp then go through the below commands
        char['lvl'] += 1 #level will go up by 1
        char['xp'] = char['xp'] - char['lvlnext'] #take xp away from lvlnext to get new xp value
        char['lvlnext'] = round(char['lvlnext'] * 1.2) #make lvlnext xp increase as the char levels up
        char['ATK'] += 1 #increase base atk stat
        char['DEF'] += 1 #increase base def stat
        char['HP'] +=1 #increase base HP stat
        if char["xp"] < char["lvlnext"]: #once the char can level no more output the below to show new stats. 
            print("Congratulations you have reached level " + str(char["lvl"]))
            print("Current XP             " + str(char["xp"]))
            print("XP to next level       " + str(char["lvlnext"]))
            print("HP                   ^ " + str(char["HP"]))
            print("Attack               ^ " + str(char["ATK"]))
            print("Defense              ^ " + str(char["DEF"]))

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
def clrscrn():
    if os.name == 'posix':
        _=os.system("clear")
    else:
        _=os.system('cls')

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
    
    
char ['HP'] = char['HP'] - 100

deathseq()


input()