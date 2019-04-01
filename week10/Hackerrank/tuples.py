if __name__ == '__main__':
    n = int(raw_input())
    #integer_list = map(int, raw_input().split())
    print(hash(tuple(int(x) for x in raw_input().split())))