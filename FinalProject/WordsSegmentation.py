
def accept(Aw, i, j):
    return False

#V words in sentence
def algo1(V):
    E = []
    n = V.length
    for i in range(n):
        for j in range(i, n):
            if accept(Aw, i, j):
                E.append((i, j+1))
    return (tuple(V), tuple(E))


def fileToSentences(fileName):
    fi = open(fileName)
    sentences = []
    for line in fi:
        if line != '\n':
            line = line.strip()
            sentences.append(re.split("["+ string.punctuation + "]+", line))
    return sentences
