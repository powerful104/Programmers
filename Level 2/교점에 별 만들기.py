from numpy import Inf


def solution(line):
    
    meet = []
    maxX = -Inf
    maxY = -Inf
    
    minX = Inf
    minY = Inf
    
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
    
    width = maxX - minX
    height = maxY - minY
    
    for i in meet:
        i[0] += transX
        i[1] += transY
    print(meet)
    
    answer = [['.' for _ in range(width)] for _ in range(height)]
    
    print(answer)
    
    for i in meet:
        answer[i[0]][i[1]] = '*'
    
    for i in answer:
        i = "".join(i)
    print(answer)
    
    return answer

solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]])