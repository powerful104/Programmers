def solution(record):
    
    answer=[]
    tmpans = []
    tmpdic = {}
    for i in record:
        tmpli = i.split()
        if tmpli[0] == "Enter":
            tmpans.append(tmpli[1]+"님이 들어왔습니다.")
            tmpdic[tmpli[1]] = tmpli[2]
        elif tmpli[0] == "Leave":
            tmpans.append(tmpli[1]+"님이 나갔습니다.")
        else:
            tmpdic[tmpli[1]] = tmpli[2]
    for i in tmpans:
        answer.append(tmpdic[i[:i.find('님')]]+i[i.find('님'):])
    return answer