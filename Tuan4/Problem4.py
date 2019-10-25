import random as rd
import string
import pickle

def randomString(strLength = 5):
    letters = string.ascii_letters
    return ''.join(rd.choice(letters) for i in range(strLength))


d_obj = {}
for i in range(100):
    rand_number = rd.randrange(99999)
    rand_string = randomString()
    d_obj[rand_number] = rand_string
pickle.dump(d_obj, open('dict.dat', 'wb'))
d_obj_read = pickle.load(open('dict.dat', 'rb'))
for e in d_obj_read:
    print(str(e) + "\t" + d_obj_read[e])
