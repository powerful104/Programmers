name = "JEROEN"
unco = [i for i in range(len(name)) if name[i] != 'A' ]
print(unco)
cur = 0
answer = 0
if unco[0] >= len(name)-unco[-1] + cur:
    cur = unco[0]
    answer += unco[0]
else:
    cur = unco[-1]
    answer += len(name)-unco[-1] + cur

"""

"""