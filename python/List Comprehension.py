if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listOfX= [i for i in range(x+1)]
    listOfY = [i for i in range(y+1)]
    listOfZ = [i for i in range(z+1)]
    
    def coordinateCreate(xcord,ycord,zcord):
        tempHold = []
        for i in xcord:
            for j in ycord:
                for k in zcord:
                    tempHold.append([i,j,k])
        return tempHold
    
    allPosVal = coordinateCreate(listOfX,listOfY,listOfZ)
    correctVal = [i for i in allPosVal if sum(i) != n]
    print(correctVal)
    
