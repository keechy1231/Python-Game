import math
import os  


health = 10
stamina= 10
mana = 10
stealth = 10
strength = 10

health = health * 3
stamina = stamina * 2
mana = mana * 4
stealth = stealth * 1
strength = strength * 5
#print("A Paladin you will be!\nYour strength and mana are you best assets but you have okay cardio after all that jogging.\nYou are not really the best at hiding in that plate mail though *$%CLING?!@CLANG@#*.")


from enemy import Imp, Dwarf, Ogre


Imp.Ehealth = Imp.Ehealth + 50
print   (Imp.Ehealth)
input()

while (Imp.Ehealth>0) and (health>0):
    print("choose an attack.\n1.slash\n2.stab\n")
    attack = input()
    if (attack == "1") or (attack == "slash"):
        (Imp.Ehealth) = (Imp.Ehealth) - strength
        print("Imp took " + str(strength)+ " damage.")
    if (Imp.Ehealth>0):
        print("Imp attacks")
        health = health - Imp.Estrength
        print("You take " + str(Imp.Estrength) +" damage.")
    print ("enemy health" + str(Imp.Ehealth))
    print ("health" + str(health))
