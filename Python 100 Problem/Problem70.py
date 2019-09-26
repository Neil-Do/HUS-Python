def evenNumberCheck(l):
    try:
        assert isinstance(l, list),"Parameter is not list."
        for e in l:
            assert e % 2 == 0,"List has odd number."
    except AssertionError as err:
        print(err)
    finally:
        print("Function end.")


l = [2, 4, 6, 8, 0]
evenNumberCheck(l)
