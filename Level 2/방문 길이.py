def solution(dirs):
    dirN = {"R":0, "D":1, "L":2, "U":3}
    dirX = (1,0,-1,0)
    dirY = (0,1,0,-1)
    curX=0
    curY=0
    Path = []
    for i in dirs:
        if (i == "R" and curX != 5) or (i == "L" and curX != -5) or (i == "D" and curY != 5) or (i == "U" and curY != -5):
            oneDir = [(curX,curY),(curX + dirX[dirN[i]],curY + dirY[dirN[i]])]
            oneDir.sort()
            if oneDir not in Path:
                Path.append(oneDir)
            curX += dirX[dirN[i]]
            curY += dirY[dirN[i]]
    return len(Path)

"""
튜플을 통해 어느좌표에서 어느 좌표로 이동했는지 기록후 중복 되는 경로를 지우기 위해 정렬후 내부에 이미 중복되는 경로가 있는지 확인 후
경로를 저장하는 리스트에 넣었다.
계속 실패가 떠서 까다로운 문제였다.

방향을 기록하는 방법이 다른사람의 코드엔 조금 다른 방식으로 되어있었다.
d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
다음에는 해당 코드처럼 작성해 보는 것도 괜찮겠다고 생각했다.
"""