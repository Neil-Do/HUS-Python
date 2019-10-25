import os

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    for file in listOfFile:
        if os.path.isdir("./" + file):
            print(file)
    # allFiles = list()
    # for entry in listOfFile:
    #     fullPath = os.path.join(dirName, entry)
    #     if os.path.isdir(fullPath):
    #         allFiles = allFiles + getListOfFiles(fullPath)
    #     else:
    #         allFiles.append(fullPath)
    return None


allFiles = getListOfFiles("/media/neil-do/Intersection/MegaSync/MEGAsync/Study/Python")
# for e in allFiles:
#     print(e)
