from re import findall
from collections import Counter

def solution(s):
    numbers = Counter(findall("\d+", s))
    answer=[]
    for i in numbers.most_common():
        answer.append(int(i[0]))
    return answer