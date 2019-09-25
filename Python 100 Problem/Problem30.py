def compareStringLen(s1, s2):
    try:
        if len(s1) > len(s2):
            print(s1)
        elif len(s2) > len(s1):
            print(s2)
        else:
            print(s1)
            print(s2)
    except:
        print("Tham so ham compareStringLen khong phai la chuoi.")


compareStringLen("Hello", "World")
compareStringLen("Captain", "America")
compareStringLen("Avenger", "Marvel")
compareStringLen("Vietnam", 123)
