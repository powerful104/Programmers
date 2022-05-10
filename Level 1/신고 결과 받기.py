def solution(id_list, report, k):
    dict = {string : i for i,string in enumerate(id_list)}
    li = [[] for _ in range(len(id_list))]
    for i in report:
        name, report_name = i.split()
        li[dict[name]].append(report_name)
    
    for i in li:
        i = set(i)
        print(i)
    
    answer = []
    return answer


solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)