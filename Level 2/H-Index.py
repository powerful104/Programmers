def solution(citations):
    answer = 0
    under = []
    citations.sort()
    for i in range(1001):
        while len(citations) != 0 and citations[0] < i:
            under.append(citations[0])
            del citations[0]
        if len(under) <= i and len(citations) >= i:
            answer = i
    return answer

"""
더 간단하게 푸는 방법이 있을텐데 더 복잡하게 푼것 같다

논문의 범위가 0 부터 1000이여서
H의 범위도 당연히 0부터 1000일것이라 생각하고 0부터 1000까지의 반복을 통해 H를 직접 구했다
"""