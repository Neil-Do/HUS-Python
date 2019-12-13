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
        # self.dicmap = None
        # self.strmap = None
        # self._problem


    def convert(self, sentence):
        # delete control characters, such as Return, tabs, ... and SPACE
        sentence = sentence.strip()
        for i in range(self.WINDOW_LENGTH):
            sentence = "BOS " + sentence + " BOS"
            self.vfeats = self.feats.token(sentence, self.reference)


    def itostr(self, x):
        ans = ""
        ans = (x < 0) and "-" or "+"
        if x < 0: x = -x;
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
