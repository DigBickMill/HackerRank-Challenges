if __name__ == '__main__':
    N = int(input())
    totalList = []
    for i in range(N):
        command = input().split(' ')
        if command[0] == "insert":
            totalList.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(totalList)
        elif command[0] == "remove":
            totalList.remove(int(command[1]))
        elif command[0] == "append":
            totalList.append(int(command[1]))
        elif command[0] == "sort" :
            totalList.sort()
        elif command[0] == "pop" :
            totalList.pop()
        elif command[0] == "reverse" :
            totalList.reverse()
