def solution(routes):
    answer = 0
    routes = sorted(routes, key = lambda x:x[1])
    cursor = 0
    while(True):
        end = routes[cursor][1]
        answer += 1
        while(True):
            if len(routes) != cursor and routes[cursor][0] <= end <= routes[cursor][1]:
                cursor += 1
            else:
                break
        if len(routes) == cursor:
            break
    
    return answer

    """
    greedy 라는 태그를 보고 풀이 방법이 쉽게 생각이 났다.
    다른사람의 풀이도 나와 비슷한걸로 보아 해당 방법이 가장 효율적인 듯 하다.
    변수의 개수 등에만 약간의 차이가 있었다.
    """