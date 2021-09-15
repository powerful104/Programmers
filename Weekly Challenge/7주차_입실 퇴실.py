enter = [3,2,1]
leave = [1,3,2]

enterLi = [0]*len(enter)
leaveLi = [0]*len(leave)
answer = []

num = 0
for i in leave:
    tmp = enter.index(i)
    if tmp > num:
        num = tmp
    leaveLi[i-1] = num

num = 1001
for i in reversed(enter):
    tmp = leave.index(i)
    if tmp < num:
        num = tmp
    enterLi[i-1] = num

for i in range(len(enter)):
    cnt = 0
    for j in range(len(enter)):
        if i != j and (enterLi[i]==enterLi[j] or leaveLi[i]==leaveLi[j]):
            cnt += 1
    answer.append(cnt)
print(answer)