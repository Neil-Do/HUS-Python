import Configure
class StrMap():

    def __init__(self, smap_={}, size_=1):
        self.smap_ = smap_
        self.size_ = size_

    def getNum(self, str, ref):
        if str not in self.smap_:
            if ref == configure.LEARN:
                num = self.size_
                self.smap_[str] = num
                self.size_ += 1
                return num
            else:
                return self.size_ + 1
        else:
            return self.smap_[str]


    def size(self):
        return self.size_


    def insert(self, pa): # pa := (string, number)
        self.smap_[pa[0]] = pa[1]
        self.size_ += 1


    def print(self, mapfile):
        fileOutput = open(mapfile, 'w')
        fileOutput.write(str(len(self.size_)))
        for str in self.smap_:
            fileOutput.write(str + ' ' + str(self.smap_[str]))
        fileOutput.close()


    def load(self, path):
        fileInput = open(path, 'r')
        size_ = fileInput.readline()
        for line in fileInput:
            map = line.strip().split()
            self.smap_[map[0]] = int(map(1))
        self.size_ = size_
        return True
