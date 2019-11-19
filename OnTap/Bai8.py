import operator

fi = open("Bai8Input", 'r')
l = []
for line in fi:
    l.append(tuple(line.rstrip().split(",")))
l.sort(key=operator.itemgetter(1, 2, 0))
print(l)
