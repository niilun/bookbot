# Count chars in text
def count_chars(text):
    chars_dictionary = {}
    for char in text.lower():
        if char in chars_dictionary:
            chars_dictionary[char] += 1
        else:
            chars_dictionary[char] = 1

    return chars_dictionary

# Count vowels and consonants
def count_vowels_and_consonants(text):
    valid_vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    consonant_count = 0

    for char in text.lower():
        if char in valid_vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    
    return vowel_count, consonant_count