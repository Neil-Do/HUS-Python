#
# def accept(Aw, i, j):
#     return False
#
# #V words in sentence
# def algo1(V):
#     E = []
#     n = V.length
#     for i in range(n):
#         for j in range(i, n):
#             if accept(Aw, i, j):
#                 E.append((i, j+1))
#     return (tuple(V), tuple(E))


#create vietnamese syllables dictionary
fVNSyl = open("data/VNsyl.txt")
vnSyllables = {}
for line in fVNSyl:
    line = line.strip()
    # line == syllable
    vnSyllables[line] = True
fVNSyl.close()


# create vietnamese wordlist dictionary
fwordlist = open("data/wordlist.txt")
wordlist = {}
for line in fwordlist:
    line = line.strip()
    # line == syllable
    wordlist[line] = True
fwordlist.close()


def fileToSentences(fileName):
    fi = open(fileName)
    sentences = []
    for line in fi:
        if line != '\n':
            line = line.strip()
            sentences.append(re.split("["+ string.punctuation + "]+", line))
    return sentences


if __name__ == "__main__":
