# CowboyChords

What 6-string guitar tunings have the most “Cowboy Chords”?

## What’s a guitar?

OK, a guitar is a thing that makes music.  If you don’t know what
a guitar sounds like, just Google “Eric Clapton” (according to
_Rolling Stone_, the world’s greatest living guitarist) and listen to
some of his music.

Anyway, those guitars have six strings, and sound really nice when 
they play what’s known as a chord.  A chord is simply a combination
of notes that sounds nice to listen to.  Most songs have chords; there’s
a joke that all a rock song needs is “three chords and the truth.” 

To play a chord, one pushes down some of the strings with one hand while
strumming or playing the strings with the other hand.  

A “Cowboy Chord” or open chord is a type of chord that is easy to play.

A guitar needs to be tuned or it sounds really bad.  There are a lot of
possible ways to tune guitars; the most common tuning is called EADGBE
(Elephants And Dogs Grow Big Ears, or Eddie Ate Dynamite, Good Bye
Eddie!) and most guitar music uses this tuning.  Not only does EADGBE
sound really nice in and of itself, it allows for a number of different
Cowboy Chords so people can fairly quickly make nice music with a guitar,
and is regular enough to make it pretty easy to play guitar solos (Guitar
Solo: Listen to Eddie Van Halen, anouther famous guitarist, play one
between 3:00 and 3:40 of Michael Jackson’s 1980s hit “Beat It”)

However, experienced guitar players like playing with other possible ways
to tune guitars, and this program attempts to answer an open question
about guitar tunings.

There is a lot of musical theory one will need to understand before 
being able to read and understand the next section.

## What this program does

This program finds out how many possible Cowboy Chords one can play in 
a given guitar tuning.  A Cowboy Chord is a chord that:

* Can be played with three or less fingers holding down frets
* Only the first three frets are fingered when playing the chord
* The highest pitched six, five, or four strings are stummed when playing
  the chord
* The chord is either a major triad or minor triad
* While not a factor for some guitarists, the program requires that
  the root of the chord is the lowest note played when being strummed.
  This can be disabled by putting setting ROOTLOWSTRING to be 0.
* While no standard Cowboy Chords double the third, this program allows
  the third to be doubled.

