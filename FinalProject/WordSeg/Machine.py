import Configure
import Feats
import DicMap
import StrMap
import SylMap
import liblinear.liblinear as lln


class Machine():

    def __init__(self, window_length, path, ref):

        self.WINDOW_LENGTH = window_length
        self.PATH = path
        self.index_SPACE = 1
        self.index_UNDER = 2
        self.reference = ref
        self.feats = Feats.Feats()
        self._model = lln.model
        # vector<featuresOfSyllabel>*
        self.vfeats = []
        if ref == Configure.LEARN:
            extract("một ví_dụ", ref)
        self.dicmap = None
        self.strmap = None
        self._problem = None


    def convert(self, sentence):
        # delete control characters, such as Return, tabs, ... and SPACE
        sentence = sentence.strip()
        for i in range(self.WINDOW_LENGTH):
            sentence = "BOS " + sentence + " BOS"
            self.vfeats = self.feats.token(sentence, self.reference)


    def itostr(self, x):
        ans = ""
        ans = (x < 0) and "-" or "+"
        if x < 0:
            x = -x
        ans += str(x) + '0'
        return ans


    # Convert a string to vfeats, extract features and put it in feats
    def extract(self, sentence, ref):
        # convert sentence(string) to vfeats;
        convert(sentence)
        length_ = len(self.vfeats)
        label = 0
        index = ''
        dummy = ''

        # debug
        for i in range(self.WINDOW_LENGTH, length_ - self.WINDOW_LENGTH - 1):
            featset = {}
            # get 1-gram
            for j in range(i - self.WINDOW_LENGTH + 1, i + 1 + self.WINDOW_LENGTH):
                index = itostr(j - i) + "|"
                syllablel = index + vfeats[j].syllabel
                featset[syllablel] = ref

                type = index + vfeats[j].type
                featset[type] = ref

            # get 2-gram
            for j in range(i - self.WINDOW_LENGTH + 1, i + self.WINDOW_LENGTH):
                index = itostr(j - i) + "||"
                syllablel_j = vfeats[j].syllabel
                syllablel_j1 = vfeats[j+1].syllabel
                featset[index + syllablel_j + ' ' + syllablel_j1] = ref

                type_j = vfeats[j].type
                type_j1 = vfeats[j+1].type
                featset[index + type_j + ' ' + type_j1] = ref

            # get Dictionary-features
            for j in range(1, MAX_WORD_LENGTH):
                for k in range(i - j + 1, i + 2):
                    dummy = vfeats[k].syllabel
                    for z in range(k + 1, k + j):
                        dummy += vfeats[z].syllabel
                    if self.dicmap.isWord(dummy):
                        # word segment is LEFT of dictionary features
                        if k == i + 1:
                            index = "L(" + itostr(k - i) + ")|"
                        # word segment is RIGHT of dictionary features
                        if k + j - 1 == i:
                            index = "R(" + itostr(k - i) + ")|"
                        # word segment is INSIDE of dictionary features
                        if k <= i and k+j-1 > i:
                            index = "I(" + itostr(k - i) + ")|"
                        featset[self.strmap.getNum(index + dummy, ref)] = ref

            #get label
            if self.vfeats[i].label == 1:
                label = index_SPACE
            else:
                label = index_UNDER
            if len(featset) > 0:
                # Feat or features = tuple<label (int), featset>
                self.feats.add((label, featset))

    # Convert a feats format to liblinear's problem struct
    def getProblem(self):
        # run by lib linear
        sizeOfFeats = self.feats.size()
        

    def delProblem(self):
        # for i in range
        pass

    def training(self):

    # x double is 0 ?
    def zero(x):
        if round(abs(x), 9) == 0:
            return True