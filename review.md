
# My thoughts on the problems

## Overall thoughts

This was my first year participating in AoC. And it was really great! I really liked that every problem is linked with a little story. And I only noticed the title alliterations when writing this file. I've written the first 12 days after solving all 12 problems, but wrote every other as I solved it.

I originally wanted to code it up in OCaml but it was too complicated to install a local OCaml interpreter - so I went with Python.

## Day 1: Report Repair

Nice and easy start - part 1 is a find two numbers that sum to 2020, and part 2 is 3 numbers. There are plenty of theoretical CS approaches to do this with lowest asymptomatic runtime (big O considerations), but it was easiest, especially with the given input size and lack of time limits, to use the naive approach. 

## Day 2: Password Philosophy

Here, the second-parters started being more interesting than "same problem just tougher". Basic computational elements required to solve part 1 become twisted, needing to either mostly copy-paste code or to refactor code to allow for both parts to be "modular". Still simple string manipulation, nice and short.

## Day 3: Toboggan Trajectory

An interesting twist on simple modular arithmetic, mixed with file parsing. Really great story, nice way to reduce 5 numbers to one in part 2.

## Day 4: Passport Processing

Honestly, annoying to write but probably more realistic as a real development task. Part 2 particularly, having to write the rules out with a million if-statements was just boring. But the "oh yeah code it up while leaving a backdoor for yourself to pass the security" is a fun little addition.

## Day 5: Binary Boarding

Extremely simple part 1 - just binary evaluation! Convenient to be coding in Python, as int parsing from specific base strings is not more complicated than adding a single argument to the int() function. However, I didn't think of a good quick solution to part 2 (which there is! Just sort and check for neighbor differences) so I did it manually.

## Day 6: Custom Customs

I think the title could have been better; Combined Customs perhaps? This was a very simple modification between part 1 and 2 to **describe** but not to **implement** - which was a bit annoying! 

## Day 7: Handy Haversacks

One of my favorites of the whole year. Yes, it's tough; yes, part 2 was the very obvious next question to ask; but it allows for so much thought and discussion. I've used a straight-up graph parse and a forward search in the graph to do it. Given that the graph is a DAG, you can use ideas from merge-find sets to reduce the final computation with each added "edge". Or you can forego all this and go through hard recursion to achieve the same results. And all are good solutions for this kind of initiative!

## Day 8: Handheld Halting

I **really** love assembly and low-level machines, so this was really great. Part 2 was also well designed - changing exactly one thing fixes it, and only one, no red herrings! Requires good input design.

## Day 9: Encoding Error

I think this was too much of a simplification of the general ideas of ciphers and cryptography. Reducing it to simple consecutive sums and number searches felt like Day 1 but make it sound more complex. Don't really know.

## Day 10: Adapter Array

Part 1 was just "sort". And part 2 was supposedly dynamic programming, but I couldn't figure out a way to code it (I don't do a lot of it). So ended up evaluating it manually from the obvious rules. Very convenient that there were never 2-wide gaps! But to be fair, incredibly funny imagery as you connect tens of adapters in a chain. 

## Day 11: Seating System

Cellular automata, in a great story and such a good twist. Very good problem, very fun to simulate. Here is where it seems like the problems go towards simulation rather than quick evaluation similar to competitive programming. I personally love it!

## Day 12: Rain Risk

Again, really not sure about the title, and this time even about the problem - the rain idea was instantly forgotten. Maybe *Naughty Navigation* or *Distanced Displacement*? But the problem itself was fun, with a great part 2 twist. Relatively easy to code too, with very similar code despite the twist.

## Day 13: Shuttle Search

First problem - simple, fun, part of the story. Part 2 was absolutely breaking the narrative but was a great way to use the Chinese Remainder Theorem! Yes, I ended up "cheating" by getting a worked out extended GCD function from wikibooks, but I couldn't be bothered here.

## Day 14: Docking Data

A bit of a forced narrative, but it ends up working out somewhat. Nice twist on part 2 but extremely reliant on good input generation - too many Xs, and we have exponential time up to 2^36 operations to do.

