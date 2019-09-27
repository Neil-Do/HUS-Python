
def setInveredIndex(arr_s):
    invertedIndex = {}
    for i in range(len(arr_s)):
        for c in arr_s[i]:
            if c not in invertedIndex:
                invertedIndex[c] = [i]
            else:
                if i not in invertedIndex[c]:
                    invertedIndex[c].append(i)
    return invertedIndex


def prob8():
    arr_s = [
    "new home sales top forecasts", "home sales rise in july", "increase in home sales in july", "vjuly new home sales rise"
    ]
    invertedIndex = setInveredIndex(arr_s)
    result = sorted(invertedIndex.items(), key = lambda kv: len(kv[1]), reverse=True)
    for e in result:
        print(e)
    print("\n\n")
    print("Cac ky tu co trong tat ca cac xau: ")
    for e in result:
        if len(e[1]) == len(arr_s):
            print(e)

prob8()
