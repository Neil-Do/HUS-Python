class Nguoi():
    pass


class Nam(Nguoi):
    def __init__(self):
        self.gender = "Nam"
    def getGender(self):
        return self.gender


class Nu(Nguoi):
    def __init__(self):
        self.gender = "Nu"
    def getGender(self):
        return self.gender


aNam = Nam()
aNu= Nu()
print (aNam.getGender())
print (aNu.getGender())
