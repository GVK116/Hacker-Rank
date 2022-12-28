import re


def valid_number(number):
    if len(number) == 10:
        if re.search(r'[789][0-9]{9}',number):
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'
for _ in range(int(input())):
    result = valid_number(input())
    print(result)

