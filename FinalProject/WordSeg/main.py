# import sys
# sys.path.append('DoTatThanh-Code/FinalProject/WordSeg/')
#
# from DicMap import DicMap
import Feats
import SylMap
import Machine
import pickle
from scipy import sparse
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from joblib import dump, load
f = Feats.Feats()
m = Machine.Machine(3, '../data/', 0)
m.load('', 'dongdu.map')
# print("Bệnh".lower())
# fi = open('../data/vndata/train2')
# count = 0
# for line in fi:
#     count += 1
#     if count % 100 == 0:
#         print(count)
#     m.extract(line, 0)
# result = m.vectorize_all_data()
result = sparse.load_npz("coo_matrix.npz")
# m.save_feats()
m.load_feats()
m.training()

# a = m.segment('Trong hoàn cảnh nghiệt ngã lúc đó , lụt và hạn hoành hành , giặc ngoại xâm hoành hành , tiền và phương tiện gần như không có gì , giống má cạn kiệt , trâu bò chết gần hết ... , mà đánh thắng được giặc đói , thắng một cách oanh liệt thì quả là một kỳ công .')
# print(a)
# print(m.vfeats)
# a = 'adfa wexcv zsdfsf'
# map = a.split()
# print(' '.join(map[:-1]))
