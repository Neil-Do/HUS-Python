from math import sqrt
with open("Problem24Input") as fInput:
    down = 0
    right = 0
    for line in fInput:
        lineData = line.strip().split(" ")
        if lineData[0] == "UP":
            down -= int(lineData[1])
        elif lineData[0] == "DOWN":
            down += int(lineData[1])
        elif lineData[0] == "LEFT":
            right -= int(lineData[1])
        elif lineData[0] == "RIGHT":
            right += int(lineData[1])
    print(round(sqrt(down**2 + right**2)))
