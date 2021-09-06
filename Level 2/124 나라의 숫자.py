def solution(n):
    word = ['1', '2', '4']
    length = 1
    org = 3

    while(org < n):
        n -= org
        length+=1
        org*=3

    answer = ''
    tmp = 3**(length-1)
    for i in range(length):
        ite = 0
        while(tmp < n):
            n -= tmp
            ite += 1
        tmp //= 3
        answer+=word[ite]
    return answer