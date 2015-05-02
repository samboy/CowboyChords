#!/bin/sh

# This script takes the output of CowboyChords.py modified to try a bunch
# of different tunings, and looks for tunings with a lot of major I-IV-V
# chord progressions using only Cowboy Chords (only first three frets used,
# only three prets pushed at a given time).

# Note that while 'delete array' for deleting an entire array has not been
# part of the POSIX spec, pretty much every implementation of AWK out there
# (GAWK, BWK AWK, Busybox AWK, etc.) supports it, and it has been accepted as
# being part of the next version of POSIX: 
# http://austingroupbugs.net/view.php?id=544

cat CowboyChords.manyTunings.out | awk '
{if($0 ~ /Tuning/){t=$0}if($0 ~ /Possible/){b="";for(a=4;a<=NF;a++){
 if($a !~ /m/ && $a !~ /7/){b = b "|" $a}}
 print t " " b}}' | sort -nr | awk -F\| '
{delete seen # Will be POSIX: http://austingroupbugs.net/view.php?id=544
 for(a=2;a<=NF;a++){seen[$a]=1}
 # Since we can’t have a hash of an array, this requires a bunch of ifs in AWK
 if(seen["E" ] == 1 && seen["A" ] == 1 && seen["B" ] == 1){ print "E A B " $1 }
 if(seen["F" ] == 1 && seen["A#"] == 1 && seen["C" ] == 1){ print "F A# C " $1}
 if(seen["F#"] == 1 && seen["B" ] == 1 && seen["C#"] == 1){ print "F B C#" $1}
 if(seen["G" ] == 1 && seen["C" ] == 1 && seen["D" ] == 1){ print "G C D " $1 }
 if(seen["G#"] == 1 && seen["C#"] == 1 && seen["D#"] == 1){ print "G#C#D#" $1}
 if(seen["A" ] == 1 && seen["D" ] == 1 && seen["E" ] == 1){ print "A D E " $1 }
 if(seen["A#"] == 1 && seen["D#"] == 1 && seen["F" ] == 1){ print "A# D# F " $1}
 if(seen["B" ] == 1 && seen["E" ] == 1 && seen["F#"] == 1){ print "B E F#" $1}
 if(seen["C" ] == 1 && seen["F" ] == 1 && seen["G" ] == 1){ print "C F G " $1}
 if(seen["C#"] == 1 && seen["F#"] == 1 && seen["G#"] == 1){ print "C#F#G#" $1}
 if(seen["D" ] == 1 && seen["G" ] == 1 && seen["A" ] == 1){ print "D G A " $1}
 if(seen["D#"] == 1 && seen["G#"] == 1 && seen["A#"] == 1){ print "D#G#A#" $1 }
}'

