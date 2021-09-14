from itertools import combinations
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
check = []
for i in range(len(relation[0])):
    li = list(combinations(range(len(relation[0])),i+1))
    for j in li:
        tmpRela = []
        for k in relation:
            tmp = []
            for l in j:
                tmp.append(k[l])
            tmpRela.append(tuple(tmp))
        tmpSet = set(tmpRela)
        if len(tmpRela) == len(tmpSet):
            check.append(list(j))
cur = 0
while True:
    cur2 = cur
    while True:
        cur2 += 1
        print(cur, cur2)
        if cur2 == len(check):
            break
        print(set(check[cur2]) | set(check[cur]))
        if len(list(set(check[cur])-(set(check[cur2]) | set(check[cur])))) == 0:
            del check[cur2]
            cur2 -= 1
    cur += 1
    if cur == len(check):
        break
print(check)
