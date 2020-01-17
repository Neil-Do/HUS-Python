import Configure
import Feats
import DicMap
import StrMap
import SylMap
import time
import numpy as np
import pickle
from scipy import sparse
from scipy.sparse import hstack, vstack, csr_matrix, save_npz, load_npz, coo_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
# from liblinear.python.liblinear import *

# from liblinear.python.liblinearutil import *

#liblinear
class Machine():

    def __init__(self, window_length, path, ref):

        self.WINDOW_LENGTH = window_length
        self.PATH = path
        self.index_SPACE = 1
        self.index_UNDER = 2
        self.reference = ref
        self.feats = Feats.Feats()
        self._model = None
        # vector<featuresOfSyllabel>*
        self.vfeats = []
        if ref == Configure.LEARN:
            pass
            # self.extract("một ví_dụ", ref)
        self.dicmap = DicMap.DicMap()
        self.strmap = StrMap.StrMap()
        self._problem = None


    def convert(self, sentence):
        # delete control characters, such as Return, tabs, ... and SPACE
        sentence = sentence.strip()
        for i in range(self.WINDOW_LENGTH):
            sentence = "BOS " + sentence + " BOS"
            self.vfeats = self.feats.token(sentence, self.reference)
            # self.vfeats = [(syllabel, type_, label), ...]

    def itostr(self, x):
        ans = ""
        ans = (x < 0) and "-" or "+"
        if x < 0:
            x = -x
        ans += str(x)
        return ans


    # Convert a string to vfeats, extract features and put it in feats
    def extract(self, sentence, ref):
        # convert sentence(string) to vfeats;
        self.convert(sentence)
        length_ = len(self.vfeats)
        label = 0
        index = ''
        dummy = ''

        # debug
        for i in range(self.WINDOW_LENGTH, length_ - self.WINDOW_LENGTH - 1):
            featset = []
            # get 1-gram
            for j in range(i - self.WINDOW_LENGTH + 1, i + 1 + self.WINDOW_LENGTH):
                index = self.itostr(j - i) + "|"
                syllablel = index + self.vfeats[j][0] # syllabel
                # print(j - i)
                idx_syllablel = self.strmap.getNum(syllablel, ref)
                featset.append(idx_syllablel)

                type_ = index + self.vfeats[j][1] # type
                idx_type = self.strmap.getNum(type_, ref)
                featset.append(idx_type)

            # get 2-gram
            for j in range(i - self.WINDOW_LENGTH + 1, i + self.WINDOW_LENGTH):
                index = self.itostr(j - i) + "||"
                syllablel_j = self.vfeats[j][0] # syllabel
                syllablel_j1 = self.vfeats[j+1][0] # syllabel
                idx_syllablel2 = self.strmap.getNum(index + syllablel_j + ' ' + syllablel_j1, ref)
                featset.append(idx_syllablel2)

                type_j = self.vfeats[j][1] # type
                type_j1 = self.vfeats[j+1][1] # type
                idx_type2 = self.strmap.getNum(index + type_j + ' ' + type_j1, ref)
                featset.append(idx_type2)
            # get Dictionary-features
            for j in range(1, Configure.MAX_WORD_LENGTH):
                for k in range(i - j + 1, i + 2):
                    dummy = self.vfeats[k][0] # syllabel
                    for z in range(k + 1, k + j):
                        dummy += ' ' + self.vfeats[z][0] # syllabel
                    if self.dicmap.isWord(dummy):
                        # word segment is LEFT of dictionary features
                        if k == i + 1:
                            index = "L(" + self.itostr(k - i) + ")|"
                        # word segment is RIGHT of dictionary features
                        if k + j - 1 == i:
                            index = "R(" + self.itostr(k - i) + ")|"
                        # word segment is INSIDE of dictionary features
                        if k <= i and k+j-1 > i:
                            index = "I(" + self.itostr(k - i) + ")|"
                        featset.append(self.strmap.getNum(index + dummy, ref))

            #get label
            if self.vfeats[i][2] == 1: # vfeats[i] label
                label = self.index_SPACE
            else:
                label = self.index_UNDER
            if len(featset) > 0:
                # Feat or features = tuple<label (int), featset>
                self.feats.add((label, featset))



    def vectorize(self, featset):
        dense_vector = np.zeros(len(self.strmap.smap_) + 1)
        for idx in featset:
            dense_vector[idx] += 1
        return coo_matrix(dense_vector)


    def vectorize_all_data(self):
        print('Start vectorize all data.')
        data_coo = coo_matrix((0, len(self.strmap.smap_) + 1))
        print('feats size: ', len(self.feats.get()))
        count = 0
        for f in self.feats.get():
            count += 1
            if count % 500 == 0:
                print(count)
            featset = f[1]
            featset_vectorize = self.vectorize(featset)
            data_coo = vstack((data_coo, featset_vectorize))
        print('Finish vectorize all data.')
        return data_coo


    def save_feats(self):
        pickle.dump(self.feats.get(), open( "test_feats.p", "wb" ))


    def load_feats(self):
        self.feats.feats_ = pickle.load(open( "train_feats.p", "rb" ))


    def getLabel(self):
        label = []
        count = 0
        for f in self.feats.get():
            # count += 1
            # if count % 500 == 0:
            #     print(count)
            label.append(f[0])
        return label
    # getproblem for liblinear
    # def getProblem(self):
    #     # run by lib linear
    #     sizeOfFeats = self.feats.size()
    #     x = [None] * sizeOfFeats # feature_node 2D arr
    #     # y = labels, space = 1, underscore = 2
    #     y = [0] * sizeOfFeats
    #
    #     for i in range(sizeOfFeats):
    #
    #         # y[i] label of sample i
    #         y[i] = self.feats.get()[i][0]
    #
    #         feature_set = self.feats.get()[i][1]
    #         # x[i] = xx = arr of feature_node, liblinear's object for sentences' features
    #         xx = [None] * (len(feature_set) + 1)
    #
    #         for j in range(len(feature_set)):
    #             idx = feature_set[j]
    #             val = 1
    #             xx[j] = feature_node(idx, val)
    #         xx[len(feature_set)] = -1
    #         x[i] = xx
    #
    #     self._problem = problem(y, x)
    #     # end getproblem for liblinear

    # def delProblem(self):
    #     self._problem = None


    # def training(self):
    #
    #     start = time.time()
    #
    #     _parameter = parameter('-s 6 -e 0.01 -c 1 -v 10')
    #     print("Training Mode. Start training...")
    #     self.getProblem()
    #     self._model = train(self._problem, _parameter)
    #     print("Finish training.")
    #
    #     end = time.time()
    #     print('Running time: ', end - start)

    def training(self):

        start = time.time()
        data_coo = sparse.load_npz("coo_matrix.npz")
        # print(X_train.shape)
        labels = self.getLabel()
        print("Training Mode. Start training...")

        from sklearn.model_selection import train_test_split
        X_train, X_test, label_train, label_test = train_test_split(data_coo, labels, test_size=0.2)

        param_grid = {'C': [0.001, 0.01, 0.1, 1, 10]}
        self._model = GridSearchCV(LogisticRegression(max_iter=10), param_grid, n_jobs=-1, pre_dispatch=16, cv=5)
        self._model.fit(X_train, label_train)

        # dump(grid, 'LGmodel.joblib')
        for i in range(3):
            print()
        print("Best cross-validation score: {:.2f}".format(self._model.best_score_))
        for i in range(3):
            print()
        print("Best parameters: ", self._model.best_params_)
        print("Best estimator: ", self._model.best_estimator_)

        print("Finish training.")

        end = time.time()
        print('Running time: ', end - start)

        lr = self._model.best_estimator_
        lr.predict(X_test)
        for i in range(3):
            print()
        print("Score: {:.2f}".format(lr.score(X_test, label_test)))
        for i in range(3):
            print()

    #x double is 0 ?
    def zero(x):
        if round(abs(x), 9) == 0:
            return True


    # def save(self, model_filename, strMap_filename):
    #     modelfile = self.PATH + model_filename + ".model"
    #     print("Save model: ", model_filename + ".model")
    #     save_model(modelfile, self._model)
    #     strMapFile = self.PATH + strMap_filename + ".map"
    #     self.strmap.save(strMapFile)


        # function close test
    # def accuracy(self):
    #     y = self._problem.y
    #     y_hat = predict(self._model, _problem.x)
    #     count = 0
    #     for i in range(len(y)):
    #         if y[i] == y_hat[i]:
    #             count += 1
    #     error_rate = 100 - count/len(y) * 100
    #     print('Error rate: ', error_rate)
    #     print('data size: ', len(y))


    def load(self, model_filename, strMap_filename, path = None):
        '''
        load(self, model_filename, strMap_filename, path = self.PATH)
        '''
        if path == None:
            path = self.PATH
        print('Loading pretrain model...')
        self._model = load('LGmodel.joblib')
        print('Success loading pretrain model...')
        print('Loading pretrain strMap...')
        self.strmap.load(path + strMap_filename)
        print('Success loading pretrain strMap...')

    def segment(self, sentence):

        self.feats = Feats.Feats()
        self.extract(sentence, Configure.PREDICT)
        if (len(self.feats.get()) == 0):
            return "Empty featset"

        ans = ''
        for i in range(self.feats.size()):
            featset = self.vectorize(self.feats.get()[1])
            print(featset.shape)
            if self._model.predict(featset) == self.index_SPACE:
                ans += self.vfeats[i + WINDOW_LENGTH][0] + Configure.SPACE
            else:
                ans += self.vfeats[i + WINDOW_LENGTH][0] + Configure.UNDER
        ans += self.vfeats[self.feats.size() + WINDOW_LENGTH][0]
        dumpy = ans.strip()
        dumpy = re.sub(r'([ _])+', r'\1', dumpy )
        return dummy
