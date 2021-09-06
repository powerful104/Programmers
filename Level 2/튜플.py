from re import findall
from collections import Counter

def solution(s):
    numbers = Counter(findall("\d+", s))
    answer=[]
    for i in numbers.most_common():
        answer.append(int(i[0]))
    return answer

"""
처음에는 각 {}기호와 ,를 나누어 나누어진 집합에서 정렬을 한 후
이전 집합에 없는 요소를 찾아서 answer에 append하는 방식을 이용하서 구현하고자 했다.

생각을 하던도중 집합 구분없이 숫자들을 풀어 많은순서대로 뽑아내면 된다는것을 알았고 간편해보여서 이 방식을 택했다.

다른 사람의 풀이를 보니 위에서 적은 방식이 가장 처음 나왔고
그 다음에 내가 처음 생각한 방식 그대로 정말 똑같이 풀이를 한 사람이 있었다.

코드를 보니 이러한 풀이를 적다가 다른 풀이로 옮기게 된게 마냥 아쉬워서
그 사람의 풀이를 여기에 적어놓겠다

def solution(s):
    answer = []

    s1 = s.lstrip('{').rstrip('}').split('},{')

    new_s = []
    for i in s1:
        new_s.append(i.split(','))

    new_s.sort(key = len)

    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))

    return answer
"""