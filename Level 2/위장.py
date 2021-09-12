def solution(clothes):
    clothesInd=[]
    newClothes=[]
    answer = 1
    for i in clothes:
        if i[1] in clothesInd:
            newClothes[clothesInd.index(i[1])] += 1
        else:
            clothesInd.append(i[1])
            newClothes.append(2)
    for i in newClothes:
        answer *= i
    return answer-1

"""
각 종류의 옷의 개수를 구하여 전부 곱하고 하나도 안입고있는 경우를 제외하여 1을 빼주면
위장의 경우의 수가 나온다.

+ 리스트 두개가 아닌 dict를 쓰는 방법이 있었는데 깜빡하고 있었다.
"""