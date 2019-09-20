account = 0
with open("Problem20Input", "r") as fileInput:
    for line in fileInput:
        lineData = line.split(" ")
        if lineData[0] == "D":
            account += int(lineData[1])
        elif lineData[0] == "W":
            account -= int(lineData[1])
print(account)
