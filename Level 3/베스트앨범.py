def solution(genres, plays):
    dic={}
    answer = []
    
    for i in range(len(genres)):
        if genres[i] in dic:
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]
    sor = sorted(dic.items(), key = lambda x: -x[1])
    sorGP = sorted(zip(genres,plays,range(len(genres))),key = lambda x: -x[1])

    for i in sor:
        check = 0
        cur = 0
        while check != 2 and cur != len(sorGP):
            if sorGP[cur][0] == i[0]:
                answer.append(sorGP[cur][2])
                check += 1
            cur += 1
    return answer

"""
너무 복잡하게 푼것 같다.
먼저 장르중에 가장 많이 재생된 장르순으로 찾고, 전체 장르와 재생순을 고유번호를 붙여 재생순으로 정렬하여
각 장르당 앞의 두개의 고유번호를 answer에 추가하게끔하였다.
"""