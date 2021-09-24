def solution(strings, n):
    return sorted(sorted(strings), key = lambda x : x[n])

"""
처음에 sorted를 한번만 했더니 처음 입력배열에서 정렬이 되어있지 않아 정렬안정성이 보장되는 sorted 특성상 정렬이 되지않은 채로
정렬이 되어버리는 문제가 있었다.
따라서 일반 정렬을 한번 한 후 조건에 맞는 정렬을 하여 문제를 해결하였다.
"""