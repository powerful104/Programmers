def solution(files):
    li = []
    for i in files:
        tmpLi=[]
        tmpLi.append(i)
        for j in range(len(i)):
            if i[j].isnumeric():
                break
        for k in range(j, j + 6):
            if not i[k].isnumeric():
                break
            if k == len(i)-1:
                k += 1
                break
        tmpLi.append(i[:j].upper())
        tmpLi.append(int(i[j:k]))
        li.append(tmpLi)
    answer = [i[0] for i in sorted(li, key = lambda x: (x[1], x[2]))]
    return answer

"""
문자열을 숫자가 나오기전까지의 인덱스를 j로 구하여 해당 인덱스 이전을 Head로 하고 인덱스를 j부터 세서 숫자가 아니거나 길이가 5넘어가면
해당 지점을 k라고 하여 j부터 k까지의 문자열을 슬라이싱하여 number로 지정하였다.
head는 upper를 취해주어 정렬, 다중조건을 이용하여 number에 의해서도 정렬하였다.

또한 안정성에 관한 얘기가 있어서 파이썬의 sorted함수를 찾아보니 안정성이 유지되는 정렬이었다.
"""