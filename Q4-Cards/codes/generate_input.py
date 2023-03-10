#!/usr/bin/python3

import random
from itertools import product

# Generate a deck of cards

suits = ['spades', 'clubs', 'diamonds', 'hearts']
value = ['a', 2,3,4,5,6,7,8,9,10,'j','q','k']

deck = list(product(suits,value))

# Input file to the mapper/reducer

data = open("cards_input.txt","w")

# Draw a random number of cards from each deck (given random number, r > 40)
# Shuffle the deck and return the first r cards

for i in range(100):
	random.shuffle(deck)
	r =  random.randint(40,52)
	print("Random number is", r)
	for i,j in deck[:r]:
		data.write(i+" "+str(j)+" ")

data.close()
