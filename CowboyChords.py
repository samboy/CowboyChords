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
MAXFINGERS = 3
ROOTLOWSTRING = 1 # If 1, the root of the chord must be the low string strummed

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

# This converts a tuning in to a list of strings for each note
def showTuning(tuning):
	out = []
	for a in range(len(tuning)):
		out.append(NOTES[tuning[a]])
	return out

# This converts the output of showTuning in to a string
def tuningString(sTuning):
	out = ""
	space = ""
	for a in range(len(sTuning)):
		b = sTuning[a]
		if(b == 'X'):
			out += space + "-"
		else:
			out += space + b
		space = " "
	return out

# Is a given array of six tuning numbers a chord? 
# This critter also takes a “strum” number, between 0 and 5, which
# is the low string of the strummed chord (0: Strum all six; 1: Strum all 
# but the "low E" string; 2: Strum just DGBE four high strings)
# Frets is an array of the frets being fingered

def isTriad(tuning, strum, frets, AllFrets):
	min = OCTAVE
	notes = []
	for a in range(OCTAVE):
		notes.append(0)
	for a in range(strum, len(tuning)):
		notes[tuning[a] % OCTAVE] = 1
	out = [-1, -1]
	for a in range(len(CHORDS)):
		for b in range(OCTAVE):
			fretcount = 0
			for c in range(len(frets)):
				if(frets[c] > 0):
					fretcount += 1
			if(fretcount <= MAXFINGERS and 
			   rotate(notes,b) == CHORDS[a]):
				out = [b, a]

	if(ROOTLOWSTRING == 1 and out[0] != tuning[strum]):
		out = [-1, -1]
	# If a chord was found, note how to strum it
	if(out != [-1, -1]):
		f = copy.deepcopy(frets)
		for a in range(strum):
			f[a] = 'X';
		line = NOTES[out[0]] + NAMES[out[1]] + " " + str(f)
		f = showTuning(tuning)
		for a in range(strum):
			f[a] = 'X';
		line += " " + tuningString(f)
		AllFrets[line] = 1
	return out

# Find the number of possible cowboy chords in a given tuning
def countCowboys(tuning, string, o, f, AllFrets):
	if(string >= len(tuning)):
		for a in range(HIGHSTRUM):
			itr = isTriad(tuning,a,f,AllFrets)
			if itr != [-1, -1]:
				o[itr[0] + (OCTAVE * itr[1])] = 1	
		return 
	for a in range(HIGHFRET):
		tmp = copy.deepcopy(tuning)
		tmp[string] += a
		tmp[string] %= 12
		f[string] = a
		countCowboys(tmp, string + 1, o, f, AllFrets)

# Given a list of possible chords for a given tuning, show that list
# as a one-liner of possible chords
def showChords(result):
	out = ""
	for o in range(OCTAVE):
		for t in range(len(CHORDS)):
			if result[(OCTAVE * t) + o] == 1:
				out += NOTES[o] + NAMES[t] + ' '
	return out
		

# For a given tuning, show the possible chords followed by the strumming
# for the chords
# If "threshold" is over 0, only show the chords and strumming if at least
# threshold number of Cowboy Chords are possible
def makeChordChart(tuning, threshold):
	for a in range(len(tuning)):
		tuning[a] = tuning[a] % OCTAVE
	o = []
	for a in range(OCTAVE * 2):
		o.append(0)
	f = []
	for a in range(len(tuning)):
		f.append(0)
	AllFrets = {}
	countCowboys(tuning, 0, o, f, AllFrets)

	if(threshold > 0):
		count = 0
		for a in range(len(o)):
			if(o[a] != 0):
				count += 1
		if count < threshold:
			return 

	print "Tuning: " + tuningString(showTuning(tuning))

	# Show all the possible chords for this tuning
	print "Possible \"Cowboy Chords\": " + showChords(o)
	# And all the fret fingerings for that tuning
	for fret in sorted(AllFrets.keys()):
		print fret

# [0, 5, 10, 3, 7, 0] is EADGBE tuning.
# Here, the array, from left to right, goes from low string to high string
# The number is the note number in the octave for the string, with E as "0"
# Since A is five semitones above E, it has value 5.  D is 10 semitones
# above E and hence is 10. G is only three semitones above E, so is 3
# Here's a full table
# E	0
# F	1
# F#/Gb	2
# G	3
# G#/Ab	4
# A	5
# A#/Bb	6
# B	7
# C 	8
# C#/Db	9
# D	10
# D#/Eb	11
makeChordChart([0, 5, 10, 3, 7, 0],7)

# Standard "E minor" blues alt tuning
#makeChordChart([0, 7, 0, 3, 7, 0],0)

# Ralph Patt’s Major Thirds tuning
#makeChordChart([0, 4, 8, 0, 4, 8],0)

# All forths tuning
#makeChordChart([0, 5, 10, 3, 8, 1],0)

# All fifths tuning (this will take special strings, I think
# This has nine "Cowboy Chords", more than the eight with standard tuning
#makeChordChart([0, 7, 2, 9, 4, 11],0)

# An interesting tuning with nine "Cowboy Chords"
# In this one, we flatten the D and G middle strings down a semitone
#makeChordChart([0, 5, 9, 2, 7, 0],0)

