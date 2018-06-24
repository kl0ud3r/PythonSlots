#!/usr/bin/env python

# Python Slot Machine #########
# Easy to play, start with 100 credits
# Min bet is 1
# Max Bet is 4 
# Bonus = 20 free spins with total payout at end. Can retrigger to add more spins.  
# $-$-$ activates the bonus game
#
#
#
#
# 7-7-7 	= 100xbet	#jackpot symbol
# 7-7-any 	= 5  xbet

# =-=-= 	= 10 xbet	#tenx symbol
# =-=-any	= 3  xbet
# 
# @-@-@ 	= 2  xbet	#consolation symbol
# @-@-any 	= 1  xbet
#
# highest line pays


##### imports #######
import re
import os
import random
import time
#####################
##### global var ####
betpattern = re.compile(r'^[\d,q]$')
wait = time.sleep
rand = random.randrange
#####################
##### functions ######


# Basic player class has Credits and name. Type test as name to receive 1000 credits, type winner to receive 1,000,000
class Player:
	def __init__(self, name, credits = 200):
		self.name = name
		if name == 'test':
			self.credits = 1000
		elif name == 'winner':
			self.credits = 1000000	
		else:
			self.credits = credits
			


# Basic symbol class, messed around with creating a rarity attribute, but didnt implement it and dropped it. Could still add it to create better/worse odds 			
class GameSymbol:
	def __init__(self, symbol, value):
		self.symbol = str(symbol)
		self.value = int(value)


# Create each Symbol and symbols list		
jackpot = GameSymbol('7', 100)
bonus = GameSymbol('$', 1)
consolation = GameSymbol('@', 2)
tenx = GameSymbol('=', 10)
symbols = [jackpot, bonus, consolation, tenx]


# To use this function, pass this function to get_payout
def get_bonus_odds():
	""" More likely to get bonus game, was used for testing bonus game function"""
	global symtup
	symbol1 = rand(1,2)
	symbol2 = rand(1,2)
	symbol3 = rand(0,4)
	symtup = (symbol1, symbol2, symbol3)
	return symtup

# To use this function, pass this function to get_payout() as the first arg
def get_odds():
	""" No extra weight for any symbol (all symbols are 1 in 4 chance)"""
	global symtup
	symbol1 = rand(0,4)
	symbol2 = rand(0,4)
	symbol3 = rand(0,4)
	symtup = (symbol1, symbol2, symbol3)
	return symtup

# Randomizer/payout function # will add odds/bonus chances later, right now its pure gambling
def get_payout(odds, gamemultiplier):
	odds()
	global amountwon
	bet = gamemultiplier
	symbol1, symbol2, symbol3 = symtup
	print('{}-{}-{}'.format(symbols[symbol1].symbol, symbols[symbol2].symbol, symbols[symbol3].symbol))
	#bonus game
	if symtup[0] == 1 and symtup[0] == symtup[1] and symtup[0] == symtup[2]:
		amountwon = bet * symbols[symtup[0]].value
		print('You won free spins!')
		player.credits = player.credits + amountwon
		wait(2)
		free_spins(bet)
	#regular payouts	
	if symtup[0] == symtup[1] and symtup[0] == symtup[2]:
		amountwon = bet * symbols[symtup[0]].value
		print('You won {} credits! 3 in a row!'.format(amountwon))
		player.credits = player.credits + amountwon
	elif symtup[0] == symtup[1] and symtup[0] != symtup[2] :
		amountwon = bet * symbols[symtup[0]].value / 2
		print('You won {} credits! 2 in a row!'.format(amountwon))
		player.credits = player.credits + amountwon	
	else:
		amountwon = 0
		print("You didnt win, try again!")	
	wait(2)
	return symtup, amountwon

# working on getting the total win to stay current if the free spins loop triggers during free spins
# Free Spins Function
def free_spins(betamt):
	bet = int(betamt)
#	try:
#		if bonus != True:
#			totalwin = int()
#	finally:	
	totalwin = int()
	for i in range(21):
		os.system('clear')
		bonus = True
		freespins = 20
		freespins -= i
		print('You have {} free spins remaining'.format(freespins))
		print(totalwin)
		get_payout(get_odds, bet)
		totalwin += amountwon
	if totalwin > 200:	
		print("Big Win!!: {} Credits!".format(totalwin))
		wait(2)
	else:
		print("You won {} credits!".format(totalwin))
		wait(2)
#	bonus = False
	return bonus


# Basic Game function
def game_layout():
	"""creates a game instance and player object"""
	print("What is your name?")
	global player
	playername = raw_input()
	player = Player(playername,)
	print ("hello {}! Here are {} credits to play".format(playername, player.credits))
	print("Have fun and Good Luck!")
	wait(2)
	running = True
	while running:
		os.system('clear')
		print("type 'q' to quit")
		print('Place your bet: type 1-4')
		print('Credits Remaining:{}'.format(player.credits))
		inp = raw_input()
		os.system('clear')
		validbet = betpattern.search(inp)
		if validbet is not None:
			if inp == 'q':
				running = False
				break
			bet = int(inp)
			if bet < 5 and bet > 0:
				player.credits = player.credits - bet
				print("Here we go you! You bet:{}".format(bet))
				wait(1)
				get_payout(get_odds, bet)			
			else:
				print("Not a valid bet!")
				wait(1)
				continue
		else:
			print("Not a valid bet!")
			wait(1)			
			continue
#########################################

game_layout()

exit()


##END######################################################################
