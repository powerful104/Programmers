def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer = ''
    turn = 1
    sig = 1
    for i in range(t*m):
        for j in convert(i,n):
            if turn == p:
                answer += j
            turn += 1
            if turn > m:
                turn = 1
            if len(answer) == t:
                sig = 0
                break
        if sig == 0:
            break
    return answer

    """
    정말 기본적으로 진수에 따른 변환을 해준뒤에 turn에 맞게 문자를 추가해주었다.
    
    뭔가 쓸데없이 어렵게 풀어나간 느낌이 든다
    하지만 다른사람의 풀이를 보니 다들 비슷하게 풀어나간것을 볼 수 있었다
    """