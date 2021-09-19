def solution(prices):
    ret = [0]*len(prices)
    nonpass_ = []
    for i in range(len(prices)):
        pass_ = []
        for j in nonpass_:
            ret[j] += 1
            if prices[i] >= prices[j]:
                pass_.append(j)
        nonpass_ = list(pass_)
        nonpass_.append(i)
    return ret

"""
나는 패스된것과 패스되지 못한것의 경우를 골라서 패스된것은 계속 가지고가고 패스되지 못하면 제외되는식으로
해당 번호의 숫자가 얼마큼 남아있나를 구하였다.

다른사람의 풀이를 보니 내 풀이와 비슷했지만 조금더 달랐고 계산하기 쉬웠다.
"""