def solution(arr):
    answer = [arr[0]]
    prv = arr[0]
    for i in arr:
        if prv != i:
            answer.append(i)
        prv = i
    return answer

"""
중복되는값은 아예 옮기지도 않으면 되는 문제였다.
"""