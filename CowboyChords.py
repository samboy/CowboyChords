#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import copy

OCTAVE = 12
CHORDS = [[1,0,0,0,1,0,0,1,0,0,0,0], # MAJOR TRIAD
	  [1,0,0,1,0,0,0,1,0,0,0,0]  # MINOR TRIAD
         ]
NOTES = ['E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C', 'C#', 'D', 'D#']
NAMES = ['','m'] # Names of chords
HIGHSTRUM = 3
HIGHFRET = 4

# Rotate a chord, to account for inversions
def rotate(notes, amount):
	out = []
	amount %= OCTAVE
	for a in range(OCTAVE):
		out.append(notes[amount])
		amount += 1
		amount %= OCTAVE
	return out

# A tuning is an array of 6 numbers between 0 and 11, corresponding to
# notes in a 12-tone chromatic scale.  0 is E, 1 is F, 2 is F#, 3 is G, etc.

# Is a given array of six tuning numbers a chord? 
# This critter also takes a “strum” number, between 0 and 5, which
# is the low string of the strummed chord (0: Strum all six; 1: Strum all 
# but the "low E" string; 2: Strum just DGBE four high strings)

def isTriad(tuning, strum, frets):
	min = OCTAVE
	notes = []
	for a in range(OCTAVE):
		notes.append(0)
	for a in range(strum, len(tuning)):
		notes[tuning[a] % OCTAVE] = 1
	out = [-1, -1]
	for a in range(len(CHORDS)):
		for b in range(OCTAVE):
			if(rotate(notes,b) == CHORDS[a]):
				out = [b, a]
	return out

# Find the number of possible cowboy chords in a given tuning
def countCowboys(tuning, string, o, f):
	if(string >= len(tuning)):
		for a in range(HIGHSTRUM):
			itr = isTriad(tuning,a,f)
			if itr != [-1, -1]:
				o[itr[0] + (OCTAVE * itr[1])] = 1	
		return 
	for a in range(HIGHFRET):
		tmp = copy.deepcopy(tuning)
		tmp[string] += a
		tmp[string] %= 12
		f[string] = a
		countCowboys(tmp, string + 1, o, f)

def showChords(result):
	out = ""
	for o in range(OCTAVE):
		for t in range(len(CHORDS)):
			if result[(OCTAVE * t) + o] == 1:
				out += NOTES[o] + NAMES[t] + ' '
	return out
		
	
o = []
for a in range(OCTAVE * 2):
	o.append(0)
tuning = [0, 5, 10, 3, 7, 0]
f = []
for a in range(len(tuning)):
	f.append(0)
countCowboys(tuning, 0, o, f)
print showChords(o)
