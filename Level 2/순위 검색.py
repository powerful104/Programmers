import bisect

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
        DB[l][j][c][s].insert(bisect.bisect_left(DB[l][j][c][s], int(information[4])),int(information[4]))
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
        for i in range(3):
            if not i in tmpl:
                continue
            tmpj = []
            if j == -1:
                tmpj = list(range(len(DB[0])))
            else:
                tmpj.append(j)
            for ii in range(2):
                if not ii in tmpj:
                    continue
                tmpc = []
                if c == -1:
                    tmpc = list(range(len(DB[0][0])))
                else:
                    tmpc.append(c)
                for iii in range(2):
                    if not iii in tmpc:
                        continue
                    tmps = []
                    if s == -1:
                        tmps = list(range(len(DB[0][0][0])))
                    else:
                        tmps.append(s)
                    for iiii in range(2):
                        if not iiii in tmps:
                            continue
                        ans += len(DB[i][ii][iii][iiii]) - bisect.bisect_left(DB[i][ii][iii][iiii],int(q[7]))
        answer.append(ans)

    return answer

"""
배열을 이용하여 빠르게 접근 하려 했지만 실패

만약 "-"일 때는 전체를 참조하도록 4중 for문을 설치하면 될지도 모른다.

+ 해당 방법을 이용하여 풀이를 진행하여 정확도는 통과하였지만 효율성에서 불통하였다.

+ DB에 값을 집어넣는 과정에서 이진탐색을 이용하여 값을 정렬하며 집어넣었고
내가 원하는 값보다 큰수들을 찾을때에도 이진탐색을 이용 해당 인덱스를 전체 개수에서 빼는식으로 큰수의 개수를 찾았다.

"""