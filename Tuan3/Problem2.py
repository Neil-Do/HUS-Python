import random

print("Chuong trinh in ra ngau nhien cac so nguyen tu 0 den n. Moi nhap n: ")
n = int(input("n: "))
numberList = []
for i in range(20):
    numberList.append(random.randint(0, n))
print("max: ", max(numberList))
print("min: ", min(numberList))
numberHistogram = {}
for i in numberList:
    if i in numberHistogram:
        numberHistogram[i] += 1
    else:
        numberHistogram[i] = 1
print(sorted(numberHistogram.items(), key=lambda x: x[1], reverse=True)[0])
