def solution(people, limit):
    answer =0
    cur1 = 0
    cur2 = len(people) - 1
    people.sort()
    while cur2 - cur1 > 0:
        if people[cur1] + people[cur2] <= limit:
            cur1 += 1
        cur2 -= 1
        answer += 1
    return answer + cur2 - cur1 + 1

"""
먼저 생각이 든 아이디어는 정렬 후 가장 앞의 원소와 가장 뒤의 원소를 비교하여 둘의 합이 limit을 넘어가면 뒤의 원소만 제외하여
전체 list의 길이가 1만남거나 아예없어질때까지 반복하는것이었다.
이것은 물론 수가 커지면 시간초과의 위험이 있어 걱정했는데 물론 시간초과가 발생했다.

처음에는 다음과 같이 풀었다
def solution(people, limit):
    answer =0
    people.sort()
    while len(people)>1:
        if people[0] + people[-1] <= limit:
            del people[0]
            del people[-1]
        else:
            del people[-1]
        answer += 1
    return answer + len(people)

따라서 시간초과를 줄이기 위해 실제 리스트를 제거하는것이 아닌
현재 계산을 진행할 무게의 커서만을 남겨 커서를 이동하는식으로 계산을 하였다.
그랬더니 시간초과가 뜨지 않았다.
"""