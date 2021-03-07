if __name__ == '__main__':
    n = int(input())
    holdNum=[1]
    
    for i in range(2,n+1):
        holdNum.append(i)
    for i in range(n):
        print(holdNum[i],end="")
