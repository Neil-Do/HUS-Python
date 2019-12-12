import re
import string


def accept(Aw, i, j):
    return False
    

def algo1(V):
    E = []
    length = len(V)
    for i in range(length):
        for j in range(length):
            if accept(Aw, i, j):
                E.append((i, j+1))
    return (tuple(V), tuple(E))


fi = open("in")
sentences = []
for line in fi:
    if line != '\n':
        line = line.strip()
        sentences.append(re.split("["+ string.punctuation + "]+", line))

count = 0
for paragraph in sentences:
    if count < 10:
        for wordGroup in paragraph:
            if wordGroup != '':
                # print(wordGroup)
                vertices, edges = algo1(wordGroup)
                for edge in edges:
                    first_word = vertices[edge[0]]
                    second_word = vertices[edge[1]]
                    print(first_word + "_" + second_word)
                count += 1
