from itertools import combinations
def solution(relation):
    check = []
    for i in range(len(relation[0])):
        li = list(combinations(range(len(relation[0])),i+1))
        for j in li:
            tmpRela = []
            for k in relation:
                tmp = []
                for l in j:
                    tmp.append(k[l])
                tmpRela.append(tuple(tmp))
            tmpSet = set(tmpRela)
            if len(tmpRela) == len(tmpSet):
                check.append(list(j))
    cur = 0
    while True:
        cur2 = cur
        while True:
            cur2 += 1
            if cur2 == len(check):
                break
            if len(list(set(check[cur])-(set(check[cur2]) & set(check[cur])))) == 0:
                del check[cur2]
                cur2 -= 1
        cur += 1
        if cur == len(check):
            break
    return len(check)
"""
가능한 모든 키의 조합을 나타낸후 해당 키의 조합에서 생기는 relation의 조합을 모두 뽑아낸후
첫번째 조건인 유일성을 만족하는지 확인후 유일성을 만족하는 키의 조합만을 남긴다
그후 키의 조합의 최소성을 만족시키기 위해서 set를 이용 중복되는값이 있다면 가장 길이가 적은 것만을 남기는 식으로 정리한다.
정답은 맞췄지만 너무 복잡하게 푼 느낌이다
"""