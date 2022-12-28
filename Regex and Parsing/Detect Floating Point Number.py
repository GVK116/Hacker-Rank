import re

pattern = re.compile('^[+-]?[0-9]*\.[0-9]+$')

for _ in range(int(input())):
    s = re.match(pattern,input())
    print(bool(s))