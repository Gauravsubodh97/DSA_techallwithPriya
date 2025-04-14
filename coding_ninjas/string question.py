
string1 = "a bb ccc dddd"

words = string1.split()
output = ' '.join([word[0] * (i + 1) for i, word in enumerate(reversed(words))])
print(output)
