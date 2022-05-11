def solution(id_list, report, k):
    dict = {string : i for i,string in enumerate(id_list)}
    report_list = [[0 for _ in range(len(id_list))] for _ in range(len(id_list))]
    ban_list = []
    answer = []
    
    for i in report:
        name, report_name = i.split()
        report_list[dict[report_name]][dict[name]] = 1
    
    for i in range(len(report_list)):
        if sum(report_list[i]) >= k:
            ban_list.append(i)
    
    for i in range(len(id_list)):
        temp = 0
        for j in ban_list:
            temp += report_list[j][i]
        answer.append(temp)
    
    return answer

    """
    너무 복잡하게 짠듯한 감이 있는 코드다.
    나중에 수정이 필요해 보인다.
    """