def pal(s):
    for i in range(len(s)//2):
        if s[i]!=s[-(1+i)]:
            return False
    return True 

def solution(s):
    mx = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if j-i <= mx:
                continue
            tmps = s[i:j]
            if pal(tmps):
                if len(tmps)>mx:
                    mx = len(tmps)
    return mx

"""
앞에서 부터 길이를 하나씩 늘려가며 문자열을 슬라이싱하여 해당 문자열이 팰린드롬인지 확인하였다.
"""