import sys
import os

result = []
if sys.argv[1] == '-s':
    print('string mode')
    result.append(sys.argv[2])
elif sys.argv[1] == '-f':
    f = open(sys.argv[2], 'r')
    count = 0
    for line in f:
        result.append(line)
        count += 1
        if count > 10:
            break
if len(sys.argv) > 3:
    if sys.argv[3] == '-o':
        fo = open(sys.argv[4], 'w')
        for line in result:
            fo.write(line + '\n')
