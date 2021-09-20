def solution(s):
    s = s.upper()
    if s.count('P') == s.count('Y'):
        return True
    return False

"""
문자의 개수만 세면 되는 간단한 문제였다.
"""