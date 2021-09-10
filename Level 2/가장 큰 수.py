def solution(numbers):
    answer = ''.join([i[:len(i)//3] for i in sorted([str(i)*3 for i in numbers], reverse = True)])
    if int(answer) == 0:
        answer = '0'
    return answer
"""
정렬 조건을 생각하기 까다로운 문제였다.
내힘으로만 푼것은 아니고 질문을 통해 힌트를 얻었다.
"""