def solution(s):
    if not (len(s) == 4 or len(s) == 6):
        return False
    for i in s:
        if not i.isnumeric():
            return False
    return True

"""
간단한 문제였다.
"""