def solution(rows, columns, queries):
    answer=[]
    maps = []
    num = 1
    for i in range(rows):
        tmpli=[]
        for j in range(columns):
            tmpli.append(num)
            num += 1
        maps.append(tmpli)

    for i in queries:
        r_1, c_1, r_2, c_2 = i
        curR = r_1
        curC = c_1
        tmp1 = maps[r_1-1][c_1-1]
        tmp2 = 0
        tmpLi=[]
        for j in range(c_1,c_2):
            tmp2 = maps[r_1-1][j]
            maps[r_1-1][j] = tmp1
            tmpLi.append(tmp1)
            tmp1 = tmp2
        for j in range(r_1,r_2):
            tmp2 = maps[j][c_2-1]
            maps[j][c_2-1] = tmp1
            tmpLi.append(tmp1)
            tmp1 = tmp2
        for j in range(c_2-2,c_1-2,-1):
            tmp2 = maps[r_2-1][j]
            maps[r_2-1][j] = tmp1
            tmpLi.append(tmp1)
            tmp1 = tmp2
        for j in range(r_2-2,r_1-2,-1):
            tmp2 = maps[j][c_1-1]
            maps[j][c_1-1] = tmp1
            tmpLi.append(tmp1)
            tmp1 = tmp2
        answer.append(min(tmpLi))
    return answer

"""
행렬을 회전시키는 문제였다
해결방안을 떠올리는데에 크게 어려움을 겪지 않은게, 회전을 해보면서 min값을 찾기만 하면 되는 문제였다
회전은 for문을 여러개 써서 진행하였고 윗줄, 오른쪽줄, 아래줄, 왼쪽줄 순으로 회전시켰다

tmp1과 tmp2를 활용하여 값을 저장후 바꾸는 방식을 사용하였고
회전되는 모든값을 tmpLi에 담아 min함수로 최솟값을 구했다

더 쉽게? 더 좋은 알고리즘이 있을것만 같은 문제이다
"""