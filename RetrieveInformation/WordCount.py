def getStopword():
    fo = open("stopword", "r")
    s = fo.readline()
    stopword_set = set(s.split(","))
    for e in stopword_set:
        print(e)


getStopword()
