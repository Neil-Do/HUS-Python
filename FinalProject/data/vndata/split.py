f = open('test_filt', 'r')
fo = open('test3', 'w')
count = 0
for line in f:
    count += 1
    if count > 100:
        break
    fo.write(line)
# sparse.save_npz("yourmatrix.npz", matrix)
