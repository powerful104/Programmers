def solution(lottos, win_nums):
    worst = 7 - len(set(lottos)&set(win_nums))
    best = worst - lottos.count(0)
    if best == 7:
        best -= 1
    if worst == 7:
        worst -=1
    return [best,worst]

"""
간단한 문제였다.
"""