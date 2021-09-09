def solution(board):
    answer = 0
    board.insert(0, [0]*len(board[0]))
    for i in range(len(board)):
        board[i].insert(0, 0)
    
    for i in range(1,len(board)):
        for j in range(1,len(board[i])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
                if board[i][j] > answer:
                    answer = board[i][j]
    return answer**2

"""
문제를 보고 두가지 방법이 생각이 났는데
하나는 정사각형의 크기를 하나씩 키워가며 만들수 있는지 확인해 보는 방안이었고
DP로 풀면 좋겠다고 생각이 들었다

만들어질수 있는 정사각형 크기를 아는 방법은 위에서 아래로 왼쪽에서 오른쪽으로 가면서
오른쪽아래 블럭이 해당블럭인 가장 큰 정사각형의 크기를 구하면 된다.
따라서 map의 위와 왼쪽을 확장한 후에 board[i][j]가 1이라면 왼쪽, 위, 왼쪽위 대각선의 블록중 최솟값에 1을 더한값을 board에 넣었다.
"""