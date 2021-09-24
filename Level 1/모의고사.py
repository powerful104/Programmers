def solution(answers):
    num1= [1,2,3,4,5]*(len(answers)//5+1)
    num2 = [2,1,2,3,2,4,2,5]*(len(answers)//8+1)
    num3 = [3,3,1,1,2,2,4,4,5,5]*(len(answers)//10+1)

    answer = [0,0,0]
    answer2 = []
    for i in range(len(answers)):
        if num1[i] == answers[i]:
            answer[0] += 1
        if num2[i] == answers[i]:
            answer[1] += 1
        if num3[i] == answers[i]:
            answer[2] += 1
    for i in range(len(answer)):
        if answer[i] == max(answer):
            answer2.append(i+1)
    return answer2

"""
1,2,3번 참가자가 찍은 리스트를 만들어 실제 정답과 비교하였다.
"""