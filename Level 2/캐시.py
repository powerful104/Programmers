def solution(cacheSize, cities):
    cache = []
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    for i in cities:
        if i.upper() in cache:
            del cache[cache.index(i.upper())]
            cache.append(i.upper())
            answer += 1
        else:
            if len(cache) == cacheSize:
                del cache[0]
            cache.append(i.upper())
            answer += 5
    return answer

"""
LRU알고리즘을 몰라서 찾아보느라 시간이 걸렸다.
그부분을 구현하기만 하면 엄청 쉬운 문제였다.
"""