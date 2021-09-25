def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr(ord("A") + (ord(s[i]) - ord("A") + n) % 26)
        elif s[i].islower():
            s[i] = chr(ord("a") + (ord(s[i]) - ord("a") + n) % 26)
    return ''.join(s)

"""
아스키코드를 이용한 간단한 문제였다.
"""