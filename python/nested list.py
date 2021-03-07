if __name__ == '__main__':
    students = []
    
    def sortScore(record):
        return record[1]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    students.sort(key=sortScore, reverse=False)
    
    secondlowest = 0
    count = 0
    secondcount = 0
    outputstudents = []
    
    for i in students:
        if count == 0:
            lowest = i[1]
        if i[1] > lowest and secondcount == 0 :
            secondlowest = i[1]
            secondcount+=1
            outputstudents.append(i[0])
        if i[1] == secondlowest:
            if not i[0] in outputstudents:
                outputstudents.append(i[0])
        count+=1
        
    outputstudents.sort(reverse=False)
    for i in outputstudents:
        print(i)
