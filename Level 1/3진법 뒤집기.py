def solution(n):
    tmp = []
    while n != 0:
        tmp.append(n % 3)
        n=n//3
    tmp.reverse()
    ans = 0
    for i in range(0,len(tmp)):
        ans += (3**i)*tmp[i]
    return ans

"""
int에 진법변환 기능이 있는것은 알았는데 3진법이 될줄은 몰랐다.
다른사람의 코드를 보니 int를 이용하여 삼진법에서 십진법으로 변환하였다.
"""