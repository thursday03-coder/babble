text = "i love pizza i hate rain i love music"
words = text.split()

pos = 0
while pos < len(words) - 1:
    print(words[pos], "->", words[pos +1])
    pos = pos + 1