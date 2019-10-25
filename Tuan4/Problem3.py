try:
    fi = open('input', 'r')
    fo = open('reverse', 'w')
    content = []
    for line in fi:
        content.append(line.strip()[::-1])
    for line in content[::-1]:
        fo.write(line + '\n')
    fi.close()
    fo.close()
except:
    print("Loi ghi file.")
finally:
    print("Finish Problem 3")
