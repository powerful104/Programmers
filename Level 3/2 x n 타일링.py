def solution(n):
    fn = 0
    fn1 = 1
    answer = fn1
    for _ in range(n):
        answer=fn+fn1
        fn=fn1
        fn1=answer
    answer=answer%1000000007
    return answer