# Count Occurrences of a Word
# Create a function called count_word_occurrences that takes a string and a target word as input and 
# returns the number of times the target word appears in the string. The function should not be case-sensitive,
#  meaning it should count occurrences regardless of the word's case.
#  Your function should use only built-in Python tools.

def count_word_occurrences(string, target_word):
    return string.lower().split().count(target_word.lower())

    # string = string.lower()
    # target_word = target_word.lower()
    # return string.split().count(target_word)
    # return string.count(target_word)

string = "The quick brown fox jumped over the lazy dog."
target_word = "the"
print(count_word_occurrences(string, target_word)) # 2
target_word = "over"
print(count_word_occurrences(string, target_word)) # 1
target_word = "dog"
print(count_word_occurrences(string, target_word)) # 1
