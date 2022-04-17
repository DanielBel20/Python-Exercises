""" Remove first n characters from a string (read n from the keyboard)
'Ana are mere' if n=3 the program will print 'are mere' """

SENTENCE = "Ana are mere"
n = int(input("Enter n: "))
SENTENCE = SENTENCE[n:]
print(SENTENCE)
