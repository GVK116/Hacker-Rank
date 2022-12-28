n = int(input())
s = set(list(map(int, input().split())))
for _ in range(int(input())):
    query = input().split()
    if query[0].lower() == 'intersection_update':
        s.intersection_update(set(map(int,input().split())))
    elif query[0].lower() == 'update':
        s.update(set(map(int,input().split())))
    elif query[0].lower() == 'symmetric_difference_update':
        s.symmetric_difference_update(set(map(int,input().split())))
    elif query[0] == 'difference_update':
        s.difference_update(set(map(int,input().split())))

print(sum(s))