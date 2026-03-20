if __name__ == '__main__':
    N = int(input())
    arr=[]
    i=0
    while i<N:
        op =input().split()
        if op[0] == "insert":
            arr.insert(int(op[1]), int(op[2]))
        elif op[0]=="append":
            arr.append(int(op[1]))
        elif op[0]=="print":
            print(arr)
        elif op[0]=="remove":
            #val = op[1]
            val = int(op[1])
            if val in arr: 
                arr.remove(val)
        elif op[0]=="sort":
            arr.sort()
        elif op[0]=="reverse":
            arr.reverse()
        elif op[0]=="pop":
            arr.pop()
        i+=1
        
