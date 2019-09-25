class CustomException(Exception):
    def __init__(self, mes):
        Exception.__init__(self, mes)


try:
    raise CustomException("Throw custom exception.")
except Exception as e:
    print(e)
