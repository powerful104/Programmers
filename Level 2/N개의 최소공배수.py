from math import gcd
def solution(arr):
    answer = arr[0]
    for i in range(1,len(arr)):
        answer = answer*arr[i]//gcd(answer,arr[i])
    return answer

"""
최대공배수와 최소공약수의 성질을 이용하여 리스트의 첫 두개의 최소공약수를 구하여 최대공배수를 계산한다
나온 최대공배수와 그다음 요소의 최대공배수를 구한다

해당과정을 반복하며 마지막요소까지의 최대공배수를 구하면 된다
"""