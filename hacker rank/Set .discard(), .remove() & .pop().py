n = int(input())
s = set(list(map(int, input().split())))
for _ in range(int(input())):
    query = input().split()
    if query[0].lower() == 'pop':
        s.pop()
    elif query[0].lower() == 'remove':
        s.remove(int(query[1]))
    elif query[0].lower() == 'discard':
        s.discard(int(query[1]))

print(sum(s))