def solution(n,a,b):
    if a > b:
        a, b = b, a
    for i in range(n):
        if a % 2 == 1 and a + 1 == b:
            break
        a = (a+1)//2
        b = (b+1)//2
    return i+1
"""
a와 b의 번호 바뀜의 규칙을 찾아 적용해주었고
a가 홀수 일때 b가 짝수이면서 a보다 1클때 둘이 만나게 되므로 조건문을 추가해서 break로 빠지게 하였다.

처음에는 a가 b보다 클경우를 생각하지않아서 오류가 났었는데
a가 b보다 클경우 두수를 swap해줘서 해결하였다.
"""