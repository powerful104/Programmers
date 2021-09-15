import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break
        tmp1 = heapq.heappop(scoville)
        tmp2 = heapq.heappop(scoville)
        heapq.heappush(scoville,tmp1 + tmp2*2)
        answer += 1
    return answer

"""
좀만 잘못 풀어도 시간초과가 날것같은 유형의 문제라 겁이났다.
문제에서 첫번째 최소값과 두번째 최소값, 결국 최소값만을 이용하므로 최소힙을 이용해 풀면 되겠다는 생각이 들었다.
따라서 파이썬의 heapq를 이용 간단하게 풀었다.
"""