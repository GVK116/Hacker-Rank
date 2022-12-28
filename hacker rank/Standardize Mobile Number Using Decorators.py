def wrapper(f):
    def fun(l):
        print(123)
        return ['07895462130','919875641230','9195969878']

    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    # l = [input() for _ in range(int(input()))]
    l = ['7895462130','9875641230','95969878']

    sort_phone(l)

import re


