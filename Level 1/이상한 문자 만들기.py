def solution(s):
    answer = ''
    i = 0
    for j in range(len(s)):
        if i%2 == 0:
            answer += s[j].upper()
        else:
            answer += s[j].lower()
        i += 1
        if s[j] == " ":
            i=0
    return answer

"""
공백만 주의해서 다시 처리하게끔 하였다.
"""