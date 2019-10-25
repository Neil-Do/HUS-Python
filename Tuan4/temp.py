import os
from faker import Faker
fake = Faker()
for i in range(100):
    name = "/media/neil-do/Intersection/MegaSync/MEGAsync/Study/Python/DoTatThanh-Code/Tuan4/textVector/file" + str(i)
    os.system('touch ' + name)
    fo = open(name, 'w')
    fo.write(fake.text())
    fo.close()
