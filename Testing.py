#this is the main game
import os
import time #importing time
import sys


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
		
		

load = "MY MASSIVE LOAD"

print (load.lower(""))
	
	
