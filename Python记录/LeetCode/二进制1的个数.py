
def count_one(n):
    count = 0
    while n&0xffffffff != 0:
        n = n&(n-1)
        count += 1
        print(n)
    print(count)


if __name__ == '__main__':
    count_one(-1)