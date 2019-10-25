import os
import re


def wordCount(wordDict, filename):
    file = open(filename, 'r')
    w_l = re.findall(r"\w+", file.read())
    for w in w_l:
        if w in wordDict:
            wordDict[w] += 1
        else:
            wordDict[w] = 1
    file.close()


def changeDict2List(topten_word, wordNumberDict):
    result = []
    for e in topten_word:
        result.append(wordNumberDict[e])
    return result


def vectorize(topten_word, filepath):
    file = open(filepath, 'r')
    w_l = re.findall(r"\w+", file.read())
    temp_dict = dict(zip(topten_word, [0 for i in range(len(topten_word))]))
    for w in w_l:
        if w in temp_dict:
            temp_dict[w] += 1
    return changeDict2List(topten_word, temp_dict)


dirName = "/media/neil-do/Intersection/MegaSync/MEGAsync/Study/Python/DoTatThanh-Code/Tuan4/textVector"
listFile = os.listdir(dirName)

wordDict = {}
for file in listFile:
    wordCount(wordDict, dirName + "/" + file)
sorted_wordDict = sorted(wordDict.items(), key=lambda kv: kv[1], reverse=True)
topten_word = []
for i in range(10):
    topten_word.append(sorted_wordDict[i][0])
print(topten_word)

textVector = {}
for file in listFile:
    fileTextVector = vectorize(topten_word, dirName + "/" + file)
    textVector[file] = fileTextVector

for e in textVector:
    print(e + "\t" + str(textVector[e]))
