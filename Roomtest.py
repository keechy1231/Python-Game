#this file is to test a room system


#make boss check function

def room1():
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("to your East there is a big black door, its open.  To your West there is a dark corridor, which way will you go? (Type E or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "E" or mvnt == "e":
            room2()
        elif mvnt == "W" or mvnt == "w":
            room3()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("W") or mvnt !=  ("w"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()
 
 

def room2():
    print ("you have entered a room, its cold, blah blah blah discriptive bits that i am no good at") #tell the player which room they are in    
    #battle_sequence()
    win = 1    
    if win == 1: #make win function
        print ("YAY you are so cool")
    elif win != 1: 
        deathseq()  #goes to the death sequence function
        
    mvnt = input("to your East there is a big black door, its open.  To your West there is a dark corridor, which way will you go? (Type E or W to proceed)")
    while 0 == 0 and mvnt != 0:
        if mvnt == "E" or mvnt == "e":
            room2()
        elif mvnt == "W" or mvnt == "w":
            room3()
        elif mvnt != ("E") or mvnt != ("e") or mvnt != ("W") or mvnt !=  ("w"):
            print("please enter a valid command")
            mvnt == 0
            mvnt = input()       


room1()
 