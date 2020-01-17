import Configure
class StrMap():

    def __init__(self, smap_={}, size_=1):
        '''
        smap_ {features string: index number}
        example: +0|lẽ 5885 in map file => smap_{'+0|lẽ': 5885}
        features string pattern:
        '''
        self.smap_ = smap_
        self.size_ = int(size_)
        self.size_ += 1

    def getNum(self, str, ref):
        '''
        return index of string key in strmap
        '''
        # print(str)
        if str not in self.smap_:
            if ref == Configure.LEARN:
                num = self.size_
                self.smap_[str] = num
                self.size_ += 1
                return num
            else:
                return 0
        else:
            return self.smap_[str]


    def size(self):
        return self.size_


    def insert(self, pa):
        '''
        insert pa in smap
        pa := (features string: index number)
        '''
        self.smap_[pa[0]] = pa[1]
        self.size_ += 1


    # write map file
    def save(self, mapfile):
        '''
        mapfile = hard link
        '''
        fileOutput = open(mapfile, 'w')
        fileOutput.write(str(len(self.size_)))
        for str in self.smap_:
            fileOutput.write(str + ' ' + str(self.smap_[str]))
        fileOutput.close()


    def load(self, path):
        '''
        line = "+0|lẽ 5885"
        map = ["+0|lẽ", 5885]
        '''
        fileInput = open(path, 'r')
        size_ = int(fileInput.readline())
        for line in fileInput:
            map = line.strip().split()
            features = ' '.join(map[:-1])
            index = map[-1]
            self.smap_[features] = int(index)
        self.size_ = size_
        fileInput.close()
        return True
