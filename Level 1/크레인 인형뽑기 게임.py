def solution(board, moves):
    answer = 0
    newLi = []
    dolls = ['0']
    for i in range(len(board[0])):
        tmpLi = []
        for j in board:
            if j[i] != 0:
                tmpLi.append(j[i])
        newLi.append(tmpLi)
    for i in moves:
        if len(newLi[i - 1]) != 0:
            doll = newLi[i - 1][0]
            del newLi[i-1][0]
            if doll == dolls[0]:
                del dolls[0]
                answer += 2
            else:
                dolls.insert(0, doll)
    return answer
"""
간단한 구현 문제였다.
"""