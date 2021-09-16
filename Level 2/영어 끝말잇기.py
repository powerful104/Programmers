def solution(n, words):
    dic = {}
    num = 0
    prvch = words[0][0]
    for i in words:
        if i not in dic and prvch == i[0]:
            dic[i] = 1
            prvch=i[-1]
            num+=1
        else:
            break
    if num == len(words):
        return [0,0]
    return [num % n+1, num // n+1]

"""
앞문자와 뒷문자의 비교와 순서가 어떻게 되는지를 따져주는 간단한 문제였다.
"""