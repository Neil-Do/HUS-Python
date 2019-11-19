input_string = " "
account = 0
while input_string != "":
    input_string = input()
    data = input_string.split(" ")
    if data[0] == "D":
        account += int(data[1])
    elif data[0] == "W":
        account -= int(data[1])
print(account)
