# Viet chuong trinh tim kiem tu khoa trong cac tep van ban.
# Tu khoa x la mot chuoi, thuc hien tim kiem x trong cac tep thu muc, ket qua tra ve la mot Danh sach cac Bo, moi phan tu trong danh sach la mot bo gom (ten tep, dong van ban dau tien chua tu khoa x trong tep), cac phan tu trong danh sach duoc sap xep theo ten tep.
# Hoan tien phuong thuc searchInFiles(x, path) trong file FileUtils.py theo mo ta o tren.
# De liet ke danh sach cac tep va thu muc trong mot thu muc trong mot thu muc co the dung phuong thuc listdir, trong module os.

import os
import re


f = open("/media/neil-do/Intersection/MegaSync/MEGAsync/Study/Python/DoTatThanh-Code/Tuan4/file1", 'r')
for line in f:
    result = re.search(r"varius", line)
    if result != None:
        print("file1 " + line)
        break


def searchInFiles(x, path):
    result_list = []
    listFile = os.listdir(path)
    for file in listFile:
        filePath = path + "/" + file
        fi = open(filePath, 'r')
        for line in fi:
            result = re.search(x, line)
            if result != None:
                result_list.append(file, line)
                break
    return result_list
