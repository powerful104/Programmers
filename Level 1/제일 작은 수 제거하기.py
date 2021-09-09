def solution(arr):
    answer = []
    if len(arr) <= 1:
        return [-1]
    del arr[arr.index(min(arr))]
    return arr

"""
간단한 문제였다
"""