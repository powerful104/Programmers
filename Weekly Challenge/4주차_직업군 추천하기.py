def solution(table, languages, preference):
    score = []
    table.sort()
    table = [i.split() for i in table]
    for i in range(len(table)):
        tmp = 0
        for j in range(len(languages)):
            if languages[j] in table[i]:
                tmp += (6-table[i].index(languages[j]))*preference[j]
        score.append(tmp)
    answer = table[score.index(max(score))][0]
    return answer