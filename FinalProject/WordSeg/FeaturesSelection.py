# from liblinear.python.liblinear import *
# from StrMap import *
from liblinear.liblinear import *

# class FeaturesSelection():
#
#     def __init__(self, PATH):
#
#         self.PATH = PATH
#
#         print('Load StrMap')
#         map_file = PATH + "dongdu.map"
#         self._strmap = StrMap()
#         self._strmap.load(map_file)
#
#         print('Load pre-model')
#         model_file = PATH + "dongdu.model"
#         # self._model = None
#         self._model = load_model(model_file)
#
#         # self.new_strmap
#
#
#     def isZero(self, x):
#
#         return round(abs(x), 9) == 0
#
#
#     def selection(self):
#
#         print('Start Selection')
#         str_map_size = self._strmap.size()
#         print('size of StrMap: ', str_map_size)
#         dummy = list(range(str_map_size + 1))
#         smap_ = self._strmap.smap_
#         for features_str in smap_:
#             dummy[smap_[features_str]] = features_str
#
#         i
#         n
#         nr_feature = self._model



# FtrSlt = FeaturesSelection('../data/')
# FtrSlt.selection()
_model = liblinear.load_model("../data/dongdu.model")
