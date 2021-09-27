import heapq
def solution(n, works):
    ans = []
    for i in works:
        heapq.heappush(ans, (-1*i,i))

    for _ in range(n):
        num = heapq.heappop(ans)
        if num[1] == 0:
            break
        heapq.heappush(ans, (-1*(num[1]-1),(num[1]-1)))
    return sum(i[1]**2 for i in ans)

"""
계속 시간초과가 나서 heapq를 이용하여 풀었다.
근데 queue에 priority queue이용했을 땐 시간초과가 떴는데 왜 heapq는 가능?
그걸 모르겠다.
"""