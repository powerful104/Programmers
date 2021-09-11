def solution(s):
    s = ' ' + s.lower()
    li = list(s)
    for i in range(1,len(li)):
        if li[i-1] == ' ' and li[i].isalpha():
            li[i] = li[i].upper()
    answer = ''.join(li[1:])
    return answer

"""
간단한 문제였다
"""