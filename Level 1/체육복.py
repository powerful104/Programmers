def solution(n, lost, reserve):
    li = [1]*n
    for i in lost:
        li[i-1] -= 1
    for i in reserve:
        li[i-1] += 1
    for i in range(len(li)):
        if li[i] == 0:
            if i-1 >= 0 and li[i-1] == 2:
                li[i-1] -= 1
                li[i] += 1
            elif i+1 < len(li) and li[i+1] == 2:
                li[i+1] -= 1
                li[i] += 1
    return len(li)-li.count(0)

"""
학생들을 처음부터 차례로 만약 체육복이 없다면 그앞사람이 여벌이 있는지 확인하고
앞사람이 여벌이 없다면 뒷사람에게 확인하는 식으로 코드를 작성하였다.
"""