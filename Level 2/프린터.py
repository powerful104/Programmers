def solution(priorities, location):
    answer = 0
    doc = [0]*len(priorities)
    doc[location]=1
    while sum(doc)!=0:
        if priorities[0]==max(priorities):
            priorities.pop(0)
            doc.pop(0)
            answer+=1
        else:
            priorities.append(priorities.pop(0))
            doc.append(doc.pop(0))
    return answer