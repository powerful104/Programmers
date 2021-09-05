def solution(scores):
    answer = ''
    scores = [list(x) for x in zip(*scores)]
    answer = ''
    for i in range(len(scores)):
        selfs = scores[i][i]
        if (selfs == max(scores[i]) or selfs == min(scores[i])) and scores[i].count(selfs) == 1:
            scores[i][i] = -1
    for i in range(len(scores)):
        n = len(scores[i])
        su = sum(scores[i])
        if scores[i][i] == -1:
            n -=1
            su +=1
        mean = su/n
        if mean >= 90:
            answer += 'A'
        elif mean >= 80:
            answer += 'B'
        elif mean >= 70:
            answer += 'C'
        elif mean >= 50:
            answer += 'D'
        else:
            answer += 'F'
    return answer