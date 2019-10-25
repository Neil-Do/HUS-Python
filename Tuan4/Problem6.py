def add_line(dict_, line):
    if line not in dict_:
        dict_[line] = 1
    else:
        dict_[line] += 1


try:
    f1 = open('file1', 'r')
    f2 = open('file2', 'r')
    f3 = open('file3', 'r')
    f1_line_dict = {}
    f2_line_dict = {}
    f3_line_dict = {}
    for line in f1:
        add_line(f1_line_dict, line)
    for line in f2:
        add_line(f2_line_dict, line)
    for line in f3:
        add_line(f3_line_dict, line)
    print(f1_line_dict == f3_line_dict)
except e:
    print(e)
finally:
    f1.close()
    f2.close()
    f3.close()
    print("Ket thuc bai 6.")
