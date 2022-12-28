def test(num):
    if num > 1:
        for i in range(2,num):
            if num%i == 0:
                return False

        return True
    else:
        return False


a = []
for num in range(100):
    if test(num):
        a.append(num)
    else:
        continue

print(a)