def solution(n, left, right):
    li = []
    for i in range(left//n+1, right//n+2):
        li += [i]*(i-1)+list(range(i,n+1))
    return li[left%n:right-n*(left//n)+1]