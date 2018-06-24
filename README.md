# PythonSlots

Simple Python game using only Standard Library Modules, not using pygame for this one.


At this time there are a few missing elements that I have identified within the script:

-Missing a check to see if player.credits == 0 and a lose screen.
So far that hasnt actually come up due to the odds being in the players favor, to where winning is the most likely outcome.

-Missing the ability to add up the Totalwin from free spins loop if it retriggers multiple times. It adds a new total for each occurence of the loop

- doesnt display the total win until the end of free spins -- would like to add that to update and display each new win during free spins

-no real odd manipulation. just uses random module to pick each symbol. This could be implemented by having random pick from 0-99 and set if loops for each range. ie if symbol1 <= 30: print("@") if symbol1 > 30 and < 50: print ("=") ect. 



Note that I am a python noob and any critisim is appreciated, but maybe dumb it down for me or provide examples!


