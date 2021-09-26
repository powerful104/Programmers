def solution(triangle):
    for i in range(len(triangle)):
        triangle[i] = [0]+triangle[i]+[0]

    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i])-1):
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
    return max(triangle[len(triangle)-1])

"""
DP를 사용하여 위에서부터 내려오면 되는 문제였다.
"""