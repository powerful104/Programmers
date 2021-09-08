def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    str1D = {}
    str2D = {}
    inter_ = 0
    union_ = 0

    for i in range(len(str1)-1):
        if  str1[i].isalpha() and str1[i+1].isalpha():
            if str1[i]+str1[i+1] not in str1D:
                str1D[str1[i]+str1[i+1]] = 1
            else:
                str1D[str1[i]+str1[i+1]] += 1

    for i in range(len(str2)-1):
        if  str2[i].isalpha() and str2[i+1].isalpha():
            if str2[i]+str2[i+1] not in str2D:
                str2D[str2[i]+str2[i+1]] = 1
            else:
                str2D[str2[i]+str2[i+1]] += 1

    for key, value in str1D.items():
        if key in str2D:
            inter_ += min(str1D[key],str2D[key])
        union_ += str1D[key]
    for key, value in str2D.items():
        union_ += str2D[key]
    union_ -= inter_
    
    if union_ == 0:
        answer = 65536
    else:
        answer = int(65536 * inter_ / union_)
    return answer

"""
처음 문제를 보고 그다지 어렵지 않다고 생각이 들었다
요소의 개수를 세야해서 집합 자료형이 아닌 딕셔너리 자료형을 사용해야 겠다고 생각했다

딕셔너리 자료형을 이용하여 별다른 어려움없이 문제를 풀었다

다른 사람의 풀이를 보니 집합자료형으로 변환후 문자열에서 해당요소의 개수를 세서 union과 inter를 구하는것을 보았다
개수만 세면 되니 그런 방법도 통했을텐데 미처 생각하지못했다
"""