def solution(maps):
    dir = [(1,0), (0,1), (-1,0), (0,-1)]

    #map 재구성
    x = len(maps[0])
    y = len(maps)
    for i in maps:
        i.insert(0,0)
        i.append(0)
    maps.insert(0,[0]*(x+2))
    maps.append([0]*(x+2))

    #BFS
    queue =[(1,1)]
    maps[1][1] = -1
    while len(queue) != 0:
        curX = queue[0][0]
        curY = queue[0][1]
        del queue[0]
        for i in dir:
            if maps[curY+i[1]][curX+i[0]] > 0:
                queue.append((curX+i[0],curY+i[1]))
                maps[curY+i[1]][curX+i[0]] = maps[curY][curX]-1
    if maps[y][x] > 0:
        answer = -1
    else:
        answer = -maps[y][x]
    return answer

"""
문제를 보자 BFS를 이용해야겠다는 생각이들었다.
따라서 BFS를 이용하기위해 Queue를 이용하여 탐색을 해주었다
탐색을 하며 목적지까지의 거리를 계산해야했었는데 이를 지도에서 사용되는 0, 1이 아닌 음수로 표기하게끔 하여
최적의 길을 표시해놓으며 진행하였다

map 재구성은 dir 리스트를 이용하여 어디로 진행해야할지 방향을 가리키는데 이때 맵밖으로 벗어날 경우를 대비하여
0으로 이루어진 벽을 하나 감싸서 예외처리를 하지않고도 Index Error가 생기지 않게끔 하였다.

Queue에 요소가 없을때까지 긽찾기를 진행후 만약 목적지의 값이 음수가 되어있다면 길을 제대로 찾아온것이므로 -로 양수로 바꾸어 return하고
목적지의 값이 1이라면 길을 찾지 못한것이므로 -1을 return하게 하였다

나쁘지않게 풀었다는 생각이 든다
"""