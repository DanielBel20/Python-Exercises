""" Write a Python program to get a string from a given string where all occurrences
of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t' """

SAMPLE = 'restart'
N = SAMPLE[0]
SAMPLE = SAMPLE[::-1]
SAMPLE = SAMPLE.replace(N, "$", 1)
SAMPLE = SAMPLE[::-1]
print(SAMPLE)
