from itertools import product

def solution(user_id, banned_id):
    answer = 0
    
    NoC = [[] for _ in range(len(banned_id))]
    
    ban_num = 0
    for ban in banned_id:
        user_num = 0
        for user in user_id:
            if len(ban) == len(user):
                equ = False
                for i in range(len(ban)):
                    if ban[i] != '*' and ban[i] != user[i]:
                        equ = True
                if equ == False:
                    NoC[ban_num].append(user_num)
            user_num += 1
        ban_num += 1
    for i in map(list,set(map(tuple,map(sorted,map(list,product(*NoC)))))):
        if len(i) == len(set(i)):
                 answer += 1
    return answer

    """
    조금 복잡했던 문제 같다.
    특히 마지막 부분에서 map을 이용하여 product의 결과를 후처리 해줄때 복잡했다.
    """