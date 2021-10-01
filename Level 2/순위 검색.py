
def solution(info, query):
    language = {'cpp' : 0, 'java' : 1, 'python' : 2, '-' : -1}
    job = {'backend' : 0, 'frontend' : 1, '-' : -1}
    career = {'junior' : 0, 'senior' : 1, '-' : -1}
    soulfood = {'chicken' : 0, 'pizza' : 1, '-' : -1}

    DB = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    answer = []

    for information in info:
        information = information.split()
        l = language[information[0]]
        j = job[information[1]]
        c = career[information[2]]
        s = soulfood[information[3]]
        DB[l][j][c][s].append(information[4])
    for q in query:
        ans = 0
        q = q.split()
        l = language[q[0]]
        j = job[q[2]]
        c = career[q[4]]
        s = soulfood[q[6]]
        tmpl = []
        if l == -1:
            tmpl = list(range(len(DB)))
        else:
            tmpl.append(l)
        for i in range(len(DB)):
            if not i in tmpl:
                continue
            tmpj = []
            if j == -1:
                tmpj = list(range(len(DB[0])))
            else:
                tmpj.append(j)
            for ii in range(len(DB[i])):
                if not ii in tmpj:
                    continue
                tmpc = []
                if c == -1:
                    tmpc = list(range(len(DB[0][0])))
                else:
                    tmpc.append(c)
                for iii in range(len(DB[i][ii])):
                    if not iii in tmpc:
                        continue
                    tmps = []
                    if s == -1:
                        tmps = list(range(len(DB[0][0][0])))
                    else:
                        tmps.append(s)
                    for iiii in range(len(DB[i][ii][iii])):
                        if not iiii in tmps:
                            continue
                        for num in DB[i][ii][iii][iiii]:
                            if int(num) >= int(q[7]):
                                ans += 1
        answer.append(ans)

    return answer

info =["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

print(solution(info,query))

"""
배열을 이용하여 빠르게 접근 하려 했지만 실패

만약 "-"일 때는 전체를 참조하도록 4중 for문을 설치하면 될지도 모른다.

+ 해당 방법을 이용하여 풀이를 진행하여 정확도는 통과하였지만 효율성에서 불통하였다.
"""