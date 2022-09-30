prefixes = 'JKLMNOPQ'
suffix = 'ack'
buy_a_vowel = 'u'

for letter in prefixes:
    if letter == 'O':
        print(letter + buy_a_vowel + suffix)
    elif letter == 'Q':
        print(letter + buy_a_vowel + suffix)
    else:
        print(letter + suffix)

#  Give at least three examples that show different features of string slices. 
# Describe the feature illustrated by each example. 
# Invent your own examples. Do not copy them for the textbook or any other source.

words_one = "Stamps are better than bottle caps."
words_two = "simple"
words_three = "sempla"
vowel_string = 'aeiou'

# ex2.1
def use_words_one(one):
    print(one)
    better_than = one
    new_greeting = 'Camping is' + better_than[10:23] + 'staying in a hotel.'
    print(new_greeting)
use_words_one(words_one)

# ex2.2
def use_words_two(two):
    better_than = two 

use_words_two(words_two)

# ex2.3
def use_words_three(three, vowels):
    better_than = three, vowels 

use_words_one(words_three, vowel_string)