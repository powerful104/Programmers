import math
def solution(progresses, speeds):
    answer = []

    prvCost = math.ceil((100-progresses[0])/speeds[0])
    n = 1
    for i in range(1,len(progresses)):
        tmp = math.ceil((100-progresses[i])/speeds[i])
        if tmp > prvCost:
            answer.append(n)
            n = 1
            prvCost = tmp
        else:
            n += 1
    answer.append(n)
    return answer