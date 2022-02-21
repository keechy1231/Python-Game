

char = {'lvl': 1,
        'xp' : 0,
        'lvlnext' : 10,
        'ATK': 10,
         'DEF': 5,
         'HP' : 10}


inv = {'ATKpotion': 10,
        'HPpotion': 10}

HPpotion = inv['HPpotion']

ATKpotion = inv['ATKpotion']

def useHPpotion(HPpotion):

    print ("you are using HP potion")
    nhp = inv['HPpotion'] + char['HP']
    print (nhp)



def useATKpotion(ATKpotion):
    print ("you are using an Attack potion")
    nATK = inv['ATKpotion']+char['ATK'] 
    print (nATK)   

useHPpotion(HPpotion)

useATKpotion(ATKpotion)
    