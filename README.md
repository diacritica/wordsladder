# wordsladder

## How to run it

- git clone or download repo
- Create virtualenv and install requirements.txt or make sure you have click and networkx Python libraries installed
- Run ```python wl.py --help```
- You will get
```Usage: wl.py [OPTIONS]

Options:
  -lt, --letters INTEGER   Number of letters (program might try to infer).
                           [default: 4]
  -ln, --language [en|es]  Language dictionary en|es.  [default: en]
  -s, --start TEXT         Initial word.  [default: love]
  -e, --end TEXT           Final word.  [default: dead]
  --help                   Show this message and exit.
```

- Just run ```python wl.py -ln en -s love -e dead``` to see a quick example
- Also run ```python wl.py -ln en -s starter -e dessert``` to see a much more complex (and slower) example devised by the author using none other than 7 letters!

## What's behind the problem

**wordsladder** is my personal graph theory based solution to Lewis Carroll's word ladder game.

See https://en.wikipedia.org/wiki/Word_ladder for a reference to the game rules and Donald Knuth's own approach.

This small project arose from the need to generally solve one of Martin Gardner's suggested word riddles in his book "Martin Gardner. New Mathematical Diversions" (see https://www.academia.edu/9675632/Martin_Gardner._New_Mathematical_Diversions_More_Puzzles_Problems_Games_and_Other_Mathematical_Diversions_1995_) In particular, the word doublets from Lewis Carroll (see chapter 4 of cited book).

The objective is to give two words (doublets) of the same number of letters to a person and ask that person to create a so called "word ladder" where the person starts with the initial word and by *changing only one letter at a time* and using valid words (each of equal length), arrive to the end word. One famous example is:

```
GRASS
CRASS
CRESS
TRESS
TREES
TREED
GREED
GREEN
```

There is an actually shorter ladder

```
GRASS
GRAYS
GREYS
GREES
GREEN
```

At least in English and Spanish, words of 4 or 5 letters are the best suited for the game.

Initially, I superficially approached this problem through several techniques (multidimensional vector space, backtracking, etc) but it was while driving my car to my family's countryside house for 2019's New Year's Eve that it finally struck me, graph theory held the answer. Words would be graph nodes, and edges connected pairs of words that would only differ in one letter. A path between two words is therefore a word ladder, and the shortest path between two words the best solution available for such word ladder. A simple undirected graph worked beautifully.

I then allowed myself to explore other existing solutions and saw with delight that none other than Donald Knuth had applied an identical approach and derived extra knowledge of the English vocabulary from it.

## Thanks

https://github.com/dwyl/english-words/blob/master/words_alpha.txt for words_en.txt

## Future plans

Develop a simple Flask + Svelte back/front app to allow people to play the game online and check valid answers
