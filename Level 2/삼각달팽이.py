def solution(n):
    snail = [[0]*(i+1) for i in range(n)]
    #0 : 내려가기, 1 : 오른쪽으로 이동, 2 : 올라가기
    state = [(0,1),(1,0),(-1,-1)]
    curX = 0
    curY = -1
    dirs = 0 
    num = 1
    for i in range(n, 0,-1):
        for j in range(i):
            curX += state[dirs][0]
            curY += state[dirs][1]
            snail[curY][curX] = num
            num += 1
        dirs += 1
        if dirs == 3:
            dirs = 0
    return [element for array in snail for element in array]

"""
빈 달팽이 리스트를 만들고
방향을 설정하여 해당 방향으로 처음엔 n개의 수를 쭉 나열,
그후 방향을 바꿔 해당 방향으로 n-1개의 수를 쭉 나열,
이렇게 1까지 반복하면 리스트가 완성된다.
이후 그 리스트를 내부의 리스트를 모두 합쳐 출력

리스트를 합쳐 출력하는 과정에서
sum(snail,[])
과 
[element for array in snail for element in array]
을 고민했는데 왜인지
밑의 코드가 더빠르게 동작하는 것을 보았다.
이유를 분석해봐야겠다.
"""