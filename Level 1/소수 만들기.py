def solution(nums):
    n = max(nums)*3
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            for j in range(2*i, n+1, i):
                a[j] = False
    ans = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if a[nums[i]+nums[j]+nums[k]]:
                    ans += 1
    return ans

"""
nums의 최댓값의 세배의 값을갖는(더하는 숫자가 3개라 세배) 에라토스테네스의 체를 구현
삼중 for문 이용하여 해당 조합이 순열인지 체크
조합인 combination을 import하여 이용하는 방법도 있지만 직접 구해봤다.
"""