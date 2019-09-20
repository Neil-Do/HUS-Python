# from operator import itemgetter, attrgetter
with open("Problem22Input") as fInput:
    data = [tuple(line.strip().split(",")) for line in fInput]
    print(sorted(data)) # or print (sorted(l, key=itemgetter(0,1,2)))
