# Pig Latin

message = input('Enter the english message  to translate to Pig Latin: ')

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pig_latin = []
for word in message.split():
    # Seperate the non letters at the start of this word
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pig_latin.append(prefix_non_letters)
        continue

    # Seperate the non_letters ate the end of this word
    suffix_non_letters = ''
    while not word[-1].isalpha():
        suffix_non_letters += word[-1]
        word = word[:-1]

    # Remember if the word was in uppercase or title case
    was_upper = word.upper()
    was_title = word.title()

    word = word.lower()  # Make the word lowercase for the translation

    # Seperate the consonants at the start for the translation
    prefix_consonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefix_consonants += word[0]
        word = word[1:]

    # Add the Pig Latin ending to thhe word
    if prefix_consonants != '':
        word += prefix_consonants + 'ay'
    else:
        word += 'yay'

    # Set the word back to uppercase or titlecase
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()

    pig_latin.append(prefix_non_letters + word + suffix_non_letters)

print(' '.join(pig_latin))
