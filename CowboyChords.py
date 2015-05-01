#!/usr/bin/env python
# -*- coding: utf-8 -*-

OCTAVE = 12
MAJOR = [1,0,0,0,1,0,0,1,0,0,0,0]
MINOR = [1,0,0,1,0,0,0,1,0,0,0,0]

# A tuning is an array of 6 numbers between 0 and 11, corresponding to
# notes in a 12-tone chromatic scale.  0 is E, 1 is F, 2 is F#, 3 is G, etc.

# Is a given array of six numbers a chord?  0 if not, 1 if major, 2 if
# minor.  This critter also takes a “strum” number, between 0 and 5, which
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
		notes[tuning[a] % OCTAVE] = 1
	print notes

def countCowboys(tuning):
	for a in range(3):
		isTriad(tuning,a)

countCowboys([0,5,10,3,7,0])
