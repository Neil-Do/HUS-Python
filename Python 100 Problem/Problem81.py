import zlib

s = "hello world!hello world!hello world!hello world!"
t = zlib.compress(s.encode("utf-8"))
print(t)
print(zlib.decompress(t))
