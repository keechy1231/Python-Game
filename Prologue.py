#file import
import time
import os
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
            



#defineds presets
def typing(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.05)
	
def clrscrn():
	if os.name == 'posix':
		_=os.system("clear")
	else:
		_=os.system('cls')

#base stats prior to class selection
health = 10
stamina = 10
stealth = 10
strength = 10
pcclass = "villager"

#get a PC name logged and recorded
typing ("Welcome adventurer.\n")
time.sleep(1)
typing ("Where should we begin?\n")
time.sleep(1)

#player title
typing ("First off, how about your title, do you prefer mr, miss or something else?\n")
pcpronoun = input()
time.sleep(1)

#player name
typing ("And now, how about a name, what should i call you?\n")
pcname = input()

time.sleep(1)
typing ("So you're "+pcpronoun+" "+ pcname+".\nIs that correct?\n")
time.sleep(1)
question1 = input()

#checking name is correct and fucking with the players name 
if question1 == "no" or question1 == "No":
    typing ("Oh is that so, then what is your name then?")
    pcname = input()
    typing ("So its "+ pcname+". Your sure this time? Well i dont really care anymore.\nI'm going to call you "+pcpronoun+" Indecisive for wasting my time\n")
    pcname = pcpronoun+" Indecisive"
elif question1 == "yes" or question1 == "Yes":
   typing ("Okay, glad we got that right straight off the bat, you wouldnt believe how many people get their own name wrong.\nIts embarresing to be honest\n")
elif question1 != "yes" or question1 !="Yes" or question1 !="no" or question1 !="No" :
    typing("What? thats not quite the answer to my question is it. I think im going to call you "+pcpronoun+" Ignoramus.\n")
    pcname = pcpronoun+" Ignoramus"
time.sleep(1)
clrscrn()

#class selection
typing("next question for you then " + pcname + ", what is your class?\n1.Warrior\n2.Thief\n3.Soilder\n\n\n")
question2 = input()

#warrior stats
if question2 == "Warrior" or question2 == "warrior" or question2 == "1":
    health = health * 5
    stamina = stamina * 4
    stealth = stealth * 2
    strength = strength * 3
    pcclass = "Warrior" #add to all player classes
    typing ("You are a warrior! \nYou can go all night with your health and stamina.\nI wouldnt try sneaking around though too much if i were you.\n")

#thief stats
elif question2 == "Thief" or question2 == "thief" or question2 == "2":
    health = health * 2
    stamina = stamina * 3
    stealth = stealth * 5
    strength = strength * 4
    pcclass = "Thief"
    typing ("You are a thief!\nHiding in the shadows and striking unseen.\nUnfortuanately for you though, you are very squishy.\n")

#soilder stats
elif question2 == "Soilder" or question2 == "soilder" or question2 == "3":
    health = health * 4
    stamina = stamina * 2
    stealth = stealth * 3
    strength = strength * 5
    pcclass = "Soilder"
    typing ("You are a soilder.\nTake hits and hit back harder, you can do that.\nJust like a dwarf your a natural sprinter, no marathons for you.\n")

typing ("Well then my new " + pcclass + ", I hope you are happy with the results you have here as you cant change them.\n")
time.sleep(2)
print("Health:     " + str(health))
print("Stamina:    " + str(stamina))
print("Stealth:    " + str(stealth))
print("Strength:   " + str(strength))

time.sleep(5)
clrscrn()

typing("So are you ready for an adventure then? \nOf course you are why else would you be here " + pcname + ".\n")
input()

char['xp'] = char['xp'] + 50

level(char)
