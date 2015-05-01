#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import copy

OCTAVE = 12
MAJOR = [1,0,0,0,1,0,0,1,0,0,0,0]
MINOR = [1,0,0,1,0,0,0,1,0,0,0,0]

# A tuning is an array of 6 numbers between 0 and 11, corresponding to
# notes in a 12-tone chromatic scale.  0 is E, 1 is F, 2 is F#, 3 is G, etc.

# Is a given array of six tuning numbers a chord? 
# This critter also takes a “strum” number, between 0 and 5, which
# is the low string of the strummed chord (0: Strum all six; 1: Strum all 
# but the "low E" string; 2: Strum just DGBE four high strings)

def isTriad(tuning, strum):
	min = OCTAVE
	notes = []
	for a in range(OCTAVE):
		notes.append(0)
	for a in range(strum, len(tuning)):
		if tuning[a] % OCTAVE < min:
			min = tuning[a] % OCTAVE
	for a in range(strum, len(tuning)):
		notes[(tuning[a] % OCTAVE) - min] = 1
	if notes == MAJOR:
		return min
	if notes == MINOR:
		return min + OCTAVE
	return -1

def countCowboys(tuning, string, o):
	if(string >= len(tuning)):
		for a in range(3):
			itr = isTriad(tuning,a)
			if itr:
				o[itr] = 1	
		return 
	for a in range(4):
		tmp = copy.deepcopy(tuning)
		tmp[string] += a
		tmp[string] %= 12
		countCowboys(tmp, string + 1, o)

o = []
for a in range(OCTAVE * 2):
	o.append(0)
countCowboys([0,5,10,3,7,0], 0, o)
print o
