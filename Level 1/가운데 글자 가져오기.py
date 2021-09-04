def solution(s):
    answer = s[len(s)//2-1]*((len(s) % 2-1)*(-1))+s[len(s)//2]
    return answer