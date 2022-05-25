def rotated(a):
    n = len(a)
    m = len(a[0])
    result = [[0]* n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = a[i][j]
    return result

def solution(key, lock):
    answer = False
    M = len(key)
    N = len(lock)
    
    for c in range(M+N-1):
        if answer == True:
            break
        for l in range(M+N-1):
            if answer == True:
                break
            for _ in range(4):
                if answer == True:
                    break
                lock_map = [[0 for _ in range(M+M+N-2)] for _ in range(M+M+N-2)]
                for i in range(M-1, M-1+N):
                    for j in range(M-1, M-1+N):
                        lock_map[i][j] = lock[i-(M-1)][j-(M-1)]
                
                key = rotated(key)
                
                for k_c in range(M):
                    for k_l in range(M):
                        lock_map[c+k_c][l+k_l] += key[k_c][k_l]
                
                answer = True
                for i in range(M-1, M-1+N):
                    for j in range(M-1, M-1+N):
                        if lock_map[i][j] != 1:
                            answer = False
    
    return answer

    """
    그리디로 접근하여 간단하게 풀었다.
    다만 해당 방법이 정말 효율적인지에 대해서는 모르겠다.
    
    다른사람의 풀이를 보니 이렇게 푸는게 맞아보인다.
    """