# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case

#My solution :
def is_isogram(string):
    for letter in 'azertyuiopqsdfghjklmwxcvbn':
        count = 0
        for letter_word in string:
            if letter_word.lower() == letter: #.lower() enlève les majuscules
                count += 1
            if count > 1:
                return 'False'
    return 'True'
    
#Other solutions :
def is_isogram2(string):
    return len(string) == len(set(string.lower())) # set() makes the string with only distinct caracters

#Or :
is_isogram3 = lambda x : len(set(x.lower())) == len(x)


