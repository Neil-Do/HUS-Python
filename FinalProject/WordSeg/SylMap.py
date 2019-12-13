class SylMap():

    def __init__(self):
        sylMapDataFile = open("../data/VNsyl.txt", 'r')
        size_ = sylMapDataFile.readline()
        self.syl_ = set(syllabel.strip() for syllabel in sylMapDataFile)
        sylMapDataFile.close()

    def isVNESE(self, syllabel):
        return syllabel in self.syl_


# da test
