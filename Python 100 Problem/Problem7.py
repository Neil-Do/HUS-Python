print("ABS DOC\n")
print(abs.__doc__, "\n")
print("INT DOC\n")
print(int.__doc__, "\n")
print("INPUT DOC\n")
print(input.__doc__, "\n")

def square(x):
    """
        Return x squared.
    """
    return x ** 2

print("SELF-CREATE FUNCTION DOC\n")
print(square.__doc__)
