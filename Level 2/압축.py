def solution(msg):
    answer = []
    dic = {}
    for i in range(ord("A"),ord("Z")+1):
        dic[chr(i)] = i - ord("A") + 1
    cur = 0
    while cur != len(msg):
        tmpCur = cur
        while msg[cur:tmpCur + 1] in dic and tmpCur != len(msg):
            tmpCur += 1
        answer.append(dic[msg[cur:tmpCur]])
        dic[msg[cur:tmpCur+1]] = len(dic)+1
        cur = tmpCur
    return answer

"""
커서를 만들어서 해당 커서부터 그뒤의 문자들이 dic에 속해있는지 판별후 속해있다면 tmpCur를 증가시켜서 dic에 속해있지 않은 슬라이싱을 찾는다
"""