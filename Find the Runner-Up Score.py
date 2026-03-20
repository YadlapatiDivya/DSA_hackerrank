if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr_set = set(arr)
    sorted_set = sorted(arr_set)
    print(sorted_set[-2])
    
