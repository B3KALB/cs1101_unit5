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

# ex2.1

words_one = "Stamps are better than bottle caps."

def use_words_one(one):
  
    print(one)
    
    better_than = one
    
    new_words = 'Camping is' + better_than[10:23] + 'staying in a hotel.'
    
    print(new_words)
    
use_words_one(words_one)


# ex2.2

words_two = "Simple is,"

def use_words_two(two):
    
    print(two)

    better_than = two 

    new_word = better_than[:-5] + 'y changed.'

    print(new_word)
    
use_words_two(words_two)


# ex2.3

words_three = "sempla"
vowel_string = 'aeiou'

def use_words_three(three, vowels):

    print(f'{three} is now:')
    
    fix_the_i = three[0:1] + vowels[2:-2] + three[2:]
    
    fix_the_e = fix_the_i[0:-1] + vowels[1:-3]

    print(fix_the_e)
    
use_words_three(words_three, vowel_string)


# playing around
scramble = input('Scramble: ')
def use_scrable(clean_text):
    vowel_1 = 'a'
    vowel_2 = 'e'
    vowel_3 = 'i'
    vowel_4 = 'o'
    vowel_5 = 'u'
    new_word = ''
    for letters in clean_text:
        if letters == 'a':
            new_word += vowel_2
        elif letters == 'e':
            new_word += vowel_3
        elif letters == 'i':
            new_word += vowel_4
        elif letters == 'o':
            new_word += vowel_5
        elif letters == 'u':
            new_word += vowel_1
        else:
            new_word += letters
    print(new_word)
use_scrable(scramble)

decode = input('Descramble: ')
def use_decode(code_word):
    vowel_1 = 'a'
    vowel_2 = 'e'
    vowel_3 = 'i'
    vowel_4 = 'o'
    vowel_5 = 'u'
    new_word = ''
    for letters in code_word:
        if letters == 'i':
            new_word += vowel_2
        elif letters == 'o':
            new_word += vowel_3
        elif letters == 'u':
            new_word += vowel_4
        elif letters == 'a':
            new_word += vowel_5
        elif letters == 'e':
            new_word += vowel_1
        else:
            new_word += letters
    print(new_word)
use_decode(decode)