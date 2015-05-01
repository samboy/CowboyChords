#!/usr/bin/env python

# A tuning is an array of 6 numbers between 0 and 11, corresponding to
# notes in a 12-tone chromatic scale.  0 is E, 1 is F, 2 is F#, 3 is G, etc.

# Is a given array of six numbers a chord?  0 if not, 1 if major, 2 if
# minor.  This critter also takes a “strum” number, between 0 and 5, which
# is the low string of the strummed chord (0: Strum all six; 1: Strum all 
# but the "low E" string; 2: Strum just DGBE four high strings)

def isTriad(tuning, strum):
	for a in range(strum, 6):
		print tuning[a]

def countCowboys(tuning):
	for a in range(6):
		print tuning[a]

countCowboys([0,5,10,3,7,0])
