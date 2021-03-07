if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr)
    
    highest = -100
    num2 = -100
    
    for i in arr:
        if i > highest:
            highest = i
            
    for j in arr:
        if j > num2 and j<highest:
            num2 = j
        
    print(num2)
