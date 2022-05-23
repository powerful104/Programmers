def solution(A, B):
    answer = 0
    
    A.sort()
    B.sort()
    Acursor = 0
    Bcursor = 0
    
    while(True):
        if A[Acursor] < B[Bcursor]:
            Acursor += 1
            answer += 1
        Bcursor += 1
        
        if Acursor == len(A) or Bcursor == len(B):
            break
    
    return answer