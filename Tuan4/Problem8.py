import re

s = "toi thich hoc toi thich choi"
w_l = re.findall(r"\w+", s)
twoGramDict = {}
for i in range(len(w_l) - 1):
    twoGram = w_l[i] + " " + w_l[i + 1]
    if twoGram in twoGramDict:
        twoGramDict[twoGram] += 1
    else:
        twoGramDict[twoGram] = 1
print(twoGramDict)
