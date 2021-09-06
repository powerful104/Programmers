def solution(weights, head2head):
    P_Infor = [[i+1, weights[i]] for i in range(len(weights))]

    for i in range(len(weights)):
        if head2head[i].count("W")+head2head[i].count("L") != 0:
            P_Infor[i].append(head2head[i].count("W")/(head2head[i].count("W")+head2head[i].count("L")))
        else:
            P_Infor[i].append(0)
        P_Infor[i].append(0)
        for j in range(len(weights)):
            if weights[i] < weights[j] and head2head[i][j] == "W":
                P_Infor[i][3] += 1
    P_Infor = sorted(P_Infor, key = lambda x : (-x[2], -x[3], -x[1], x[0]))
    answer = [i[0] for i in P_Infor]

    return answer