def solution(m, n, board):
    answer = 0
    newBoard = []
    for i in range(n-1,-1,-1):
        tmp = ''
        for j in range(m-1,-1,-1):
            tmp += board[j][i]
        newBoard.append(tmp)

    hasBlock = 1

    while hasBlock != 0:
        hasBlock = 0
        checkBoard = [[0]*m for j in range(n)]
        for i in range(n-1):
            for j in range(m-1):
                if newBoard[i][j] == newBoard[i+1][j] == newBoard[i][j+1] == newBoard[i+1][j+1] != '1':
                    checkBoard[i][j] = 1
                    checkBoard[i+1][j] = 1
                    checkBoard[i][j+1] = 1
                    checkBoard[i+1][j+1] = 1
                    hasBlock = 1
        for i in range(n):
            for j in range(m):
                if checkBoard[i][j] == 1:
                    newBoard[i] = newBoard[i][:j] + '1' + newBoard[i][j+1:]
                    answer += 1
            newBoard[i] = newBoard[i].replace('1',"")+"1"*newBoard[i].count('1')
    return answer

"""
먼저 행렬을 계산하기 쉽게끔 행과 열을 반전 시키고 거꾸로 돌렸다
하지만 거꾸로 돌리는과정은 굳이 필요는 없었다

checkboard를 따로 만들고 지워야할 블록들을 체크하게 하였다
조건에 맞게 지워야할 블록들이 체크되면
해당 블록들을 지우고 지워진줄에 지워진 블록개수만큼의 1을 뒤에 채워넣었다

이를 반복하면 블록이 지워지지않을때까지 sum을 구하여 answer를 냈다

다른사람의 풀이를 보니 나와 비슷하게 구현하였다

뭔가 이런 구현문제는 생각하며 푸는 재미가 있는것 같다
"""