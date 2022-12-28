for _ in range(int(input())):
    a = input()
    A = set(map(int,input().split()))
    b= input()
    B = set(map(int,input().split()))
    print(A <= B)