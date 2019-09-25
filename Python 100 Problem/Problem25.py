import re

def problem25():
    print("Chuong trinh tinh tan suat cac tu tu input. Output duoc sap xep theo bang chu cai.")
    s = input("Moi nhap vao chuoi: ")
    wordData = re.split(r'[;,\s]\s*', s)
    dWord = {}
    for word in wordData:
        if word not in dWord:
            dWord[word] = 1
        else:
            dWord[word] += 1
    print(sorted(dWord.items()))


problem25()
