def solution(participant, completion):
    partdic = {}
    compdic ={}
    for i in participant:
        if not i in partdic:
            partdic[i] = 1
        else:
            partdic[i] += 1

    for i in completion:
        if not i in compdic:
            compdic[i] = 1
        else:
            compdic[i] += 1

    for i in partdic.items():
        if (partdic[i[0]] == 1 and not i[0] in compdic) or partdic[i[0]] != compdic[i[0]]:
            return i[0]

"""
dictionary 자료형을 이용하여 참여자의 수를 센 partdic과 완주자의 수를 센 compdic으로 구별하여
두 개체의 value가 다르면 해당 key가 완주하지 못한 사람이므로 return 해주었다.
"""