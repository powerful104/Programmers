def solution(name):
    co = [int(i != "A") for i in name]
    cur = 0
    answer = 0
    while co.count(1) != 0:
        cor = list(reversed(co+co[:cur])).index(1)
        col = co[cur:]
        ans = cor + 1
        if col.count(1) == 0:
            cur -= ans
            if cur<0:
                cur += len(name)
        else:
            col = col.index(1)
            if cor + 1 < col:
                cur -= ans
                if cur<0:
                    cur += len(name)
            else:
                ans = col
                cur += col
        co[cur] = 0
        answer += ans + min(91-ord(name[cur]),ord(name[cur])-65)
    return answer

"""
먼저 가로로 어떻게 이동해야 하는가를 고려하였고, 가로의 이동 방향에 따라 직접 이동하였다.
하지만 오른쪽으로 넘어가는 경우는 제외

그러고 A가 아닌 위치만을 cur가 방문 하게 되므로 이를 이용 해당 알파벳이 되려면 몇번 최소 동작해야하는지 구하였다.
"""