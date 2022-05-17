def solution(line):
    
    meet = []
    maxX = -float('inf')
    maxY = -float('inf')
    
    minX = float('inf')
    minY = float('inf')
    
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            A = line[i][0]
            B = line[i][1]
            E = line[i][2]
            C = line[j][0]
            D = line[j][1]
            F = line[j][2]
            
            if (A*D - B*C) == 0:
                continue
            
            x = (B*F - E*D) / (A*D - B*C)
            y = (E*C - A*F) / (A*D - B*C)
            
            if x.is_integer() and y.is_integer():
                x = int(x)
                y = int(y)
                
                if maxX < x:
                    maxX = x
                
                if maxY < y:
                    maxY = y
                
                if minX > x:
                    minX = x
                
                if minY > y:
                    minY = y
                
                if [x, y] not in meet:
                    meet.append([x, y])
    
    transX = -minX
    transY = -minY
    
    width = maxX - minX + 1
    height = maxY - minY + 1
    
    for i in meet:
        i[0] += transX
        i[1] += transY
    
    tempAns = [['.' for _ in range(width)] for _ in range(height)]
    
    for i in meet:
        tempAns[i[1]][i[0]] = '*'
    
    answer = []
    
    for i in tempAns:
        answer.append(''.join(i))
    answer.reverse()
    
    return answer

    """
    너무 더럽게 푼 느낌이 있다.
    수정이 필요해 보인다.
    """