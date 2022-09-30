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