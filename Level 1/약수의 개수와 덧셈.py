def divisor(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    return cnt % 2

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if divisor(i):
            answer -= i
        else:
            answer += i
    return answer

"""
실제 약수의 개수를 구하지않고 해당 수가 제곱수일때만 홀수인것을 파악해 값을 구한 사람도 있었다.
"""