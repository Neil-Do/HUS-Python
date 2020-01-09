class DicMap():

    def __init__(self):
        self.dmap_ = {}
        dmapDataFile = open("../data/wordlist.txt")
        for word in dmapDataFile:
            self.dmap_[word.strip()] = True
        dmapDataFile.close()


    def isWord(self, str):
        return str in self.dmap_
