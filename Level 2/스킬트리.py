def solution(skill, skill_trees):
    answer = 0
    for i in skill_trees:
        tmpLi = []
        for j in i:
            if j in skill:
                tmpLi.append(j)
        if tmpLi == [skill[i] for i in range(len(tmpLi))]:
            answer += 1
    return answer

"""
skill_trees에서 skill에 없는 알파벳은 제거하고 순서가 skill의 처음부터 이어지는지 확인하는 과정을 통해 구현했다.
간단한 문제였다.
"""