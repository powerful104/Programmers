def solution(places):
    answer = []

    dir1X = [1, 1, 1, 0, -1, -1, -1, 0]
    dir1Y = [-1, 0, 1, 1, 1, 0, -1, -1]

    for i in range(len(places)):
        for j in range(5):
            places[i][j] = "OO" + places[i][j] + "OO"
        places[i].insert(0, "OOOOOOOOO")
        places[i].insert(0, "OOOOOOOOO")
        places[i].append("OOOOOOOOO")
        places[i].append("OOOOOOOOO")
        sig = 1
        for curX in range(2,7):
            for curY in range(2,7):
                if places[i][curY][curX] == 'P':
                    for dir in range(8):
                        if dir % 2 == 1:
                            if places[i][curY + dir1Y[dir]][curX + dir1X[dir]] == 'P':
                                sig = 0
                                break
                            if places[i][curY + 2 * dir1Y[dir]][curX + 2 * dir1X[dir]] == 'P' and places[i][curY + dir1Y[dir]][curX + dir1X[dir]] == 'O':
                                sig = 0
                                break
                        else:
                            if places[i][curY + dir1Y[dir]][curX + dir1X[dir]] == 'P' and (places[i][curY + dir1Y[dir-1]][curX + dir1X[dir-1]] == 'O' or places[i][curY + dir1Y[dir+1]][curX + dir1X[dir+1]] == 'O'):
                                sig = 0
                                break
                if not sig:
                    break
            if not sig:
                break
        answer.append(sig)
    return answer

"""
방향성을 확인하고 if문을 잘 끼워맞추는 문제라고 생각했다
따라서 방향성을 의미하는 dirX와 dirY를 생성했고 전체 자리를 확인해가며 조건문을 통해 거리를 지키지 않은 사람이 있나 살펴보았다
문제는 간단했다
"""