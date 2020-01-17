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
        return len(self.feats_)

    def get(self):
        return self.feats_


    # (Feature = (label, feature_set))
    def add(self, feat):
        self.feats_.append(feat)


        # type method tested, for syllabel, not word
    def type(self, word):
        # print(word)  # test code
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
        #print(VH, vt, cs, kh)
        # O : other
        # N : number
        # U : upper
        # L : lower
        if kh: return "O"
        if cs and not (VH or vt): return "N"
        if cs and (VH or vt): return "O"
        #print(self.syl_.isVNESE(word.lower()))
        if self.syl_.isVNESE(word.lower()):
            if VH: return "U"
            if vt: return "L"
        return "O"


    # preprocessing string, /* Regular Expressions */
    # regex tested
    def regex(self, text, ref):
        ans = ""

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


        # token tested
    def token(self, text, ref):
        '''
        example result: [('"', 'O', 1), ('ASEM', 'O', 1), ('5', 'N', 1), ('mở', 'L', 2), ('cửa', 'L', 1), ('để', 'O', 1), ('tăng', 'L', 2), ('cường', 'L', 1), ('hợp', 'L', 2), ('tác', 'L', 1), ('tư', 'L', 2), ('nhân', 'L', 1), ('và', 'L', 1), ('các', 'L', 1), ('chính', 'L', 2), ('phủ', 'L', 1), ('nhằm', 'L', 1), ('khuyến', 'L', 2), ('khích', 'L', 1), ('hành', 'L', 2), ('động', 'L', 1), ('tích', 'L', 2), ('cực', 'L', 1), ('từ', 'L', 1), ('phía', 'L', 1), ('các', 'L', 1), ('chủ', 'L', 1), ('doanh', 'L', 2), ('nghiệp', 'L', 1), ('"', 'O', 1), (',', 'O', 1), ('nhật', 'L', 2), ('báo', 'L', 1), ('viết', 'L', 1), ('.', 'O', 1)]

        '''
        text = self.regex(text, ref)
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
