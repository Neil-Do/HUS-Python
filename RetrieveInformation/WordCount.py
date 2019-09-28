import re

def getStopword():
    fo = open("stopword", "r")
    s = fo.readline()
    stopword_set = set(s.split(","))
    for e in stopword_set:
        print(e)


def wordCount():
    # chua loc stopword
    count = 0
    fo = open("text", 'r')
    for s in fo:
        count += len(re.findall("[a-zA-Z]\w*", s))
        # count += len(re.findall("\d\.?\d*", s))
    print(count)


wordCount()
