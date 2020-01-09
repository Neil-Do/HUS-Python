from SylMap import SylMap # from from SylMap (file) import SylMap (class)
import Configure
import re

# tuple featuresOfSyllabel (string syllabel, string type, int label )

class Feats():
    #Feat := <size_t, set<size_t>* >
    def __init__(self):
        # feats_ = dict of feats
        # feats_ = {index: list of features}
        self.feats_ = []
        self.syl_ = SylMap()

    def size(self):
        return len(feats_)

    def get(self):
        return self.feats_

    # (Feature = (syllabel, type, label))
    def add(self, syllabel, type, label):
        self.feats_.append((syllabel, type, label))

    def type(self, word):
        VH = False      # Viet Hoa
        vt = False      # viet thuong
        cs = False      # chu so
        kh = False      # ky hieu

        # Regular Expressions
        numbers = r'[0-9]'
        lower = r'[a-z]'
        upper = r'[A-Z]'

        for punc in Configure.SYMBOLS:
            if punc in word:
                kh = True
                break
        VH = re.search(upper, word) != None
        vt = re.search(lower, word) != None
        cs = re.search(numbers, word) != None

        # O : other
        # N : number
        # U : upper
        # L : lower
        if kh: return "O"
        if cs and not (VH or vt): return "N"
        if cs and (VH or vt): return "O"
        if self.syl_isVNESE(word):
            if VH: return "U"
            if vt: return "L"
        return "O"


        # preprocessing string, /* Regular Expressions */
        def regex(self, text, ref):
            string ans = ""

            # replace some UTF-8 char by one byte char
            source = ["…", "“", "”"]
            replace = ["...", "\"", "\""]
            for i in range(3):
                text = text.replace(source[i], replace[i])

            #segment symbols: a?a => a ? a
            if ref == Configure.PREDICT:
                for symb in Configure.SYMBOLS:
                    text = text.replace(symb, ' ' + symb + ' ')

            # remove consecutive space and underscore: ___ => _
            text = re.sub(r'([ _])+', r'\1', text )
            return text


        def token(self, text, ref):
            text = regex(text, ref)
            text += Configure.SPACE
            ans = []    # vector<featuresOfSyllabel>
            dummy = ()      # featuresOfSyllabel
            '''
            pos := current space|underscore position
            prev := previous space|underscore position
            segment := bool variable confirm current character is space|underscore
            '''
            pos = 0
            prev = -1
            N = len(text)
            segment = False

            for pos in range(N):
                if ref == Configure.LEARN:
                # Learning OR training
                    segment = ((text[pos] == Configure.SPACE) or (text[pos] == Configure.UNDER))
                else:
                    segment = (text[pos] == Configure.SPACE)

                if segment:
                    if pos == prev + 1:
                        prev = pos
                        continue
                    syllabel = text[prev+1:pos]
                    type_ = self.type(syllabel)
                    label = (text[pos] == Configure.SPACE) and 1 or 2
                    prev = pos
                    ans.append((syllabel, type_, label))

            return ans
