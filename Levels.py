import sys
import time
import os




def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)

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
            
    

char['xp'] = char['xp'] + 40


