def solution(sizes):
    mxW = 0
    mxH = 0
    for i in range(len(sizes)):
        if mxW < max(sizes[i]):
            mxW = max(sizes[i])
        if mxH < min(sizes[i]):
            mxH = min(sizes[i])
    return mxW*mxH

"""
세로는 무조건 큰값이 오게, 가로는 무조건 작은값이 오게하여
세로와 가로의 max를 구하여 곱해주었다.
"""