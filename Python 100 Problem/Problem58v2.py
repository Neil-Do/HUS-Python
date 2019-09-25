# Bài Python 58, Code by Quantrimang.com
import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
re2 = re.match(pat2,emailAddress)
print (re2.group(1)) 
