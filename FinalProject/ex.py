import re
import string


# def accept(Aw, i, j):
#     return False
#
#
# def algo1(V):
#     E = []
#     length = len(V)
#     for i in range(length):
#         for j in range(length):
#             if accept(Aw, i, j):
#                 E.append((i, j+1))
#     return (tuple(V), tuple(E))
#
#
# fi = open("in")
# sentences = []
# for line in fi:
#     if line != '\n':
#         line = line.strip()
#         sentences.append(re.split("["+ string.punctuation + "]+", line))
#
# count = 0
# for paragraph in sentences:
#     if count < 10:
#         for wordGroup in paragraph:
#             if wordGroup != '':
#                 # print(wordGroup)
#                 vertices, edges = algo1(wordGroup)
#                 for edge in edges:
#                     first_word = vertices[edge[0]]
#                     second_word = vertices[edge[1]]
#                     print(first_word + "_" + second_word)
#                 count += 1


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

def test():
    count = 0
    for syl in vnSyllables:
        print(syl)
        count += 1
        if count > 10:
            break

s = "machine learning: \"AI systems need the ability to acquire their own knowledge, by extracting patterns from raw data. This capability is known as machine learning\""
a = 1
b = 4
c = (a > b) and 1 or 2
print(str(c))
