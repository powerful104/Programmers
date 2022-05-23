def cvtT2N(time):
    H, M, S = map(int, time.split(':'))
    num = H * 3600 + M * 60 + S
    return num

def cvtN2T(num):
    H = str(num//3600).zfill(2)
    M = str(num%3600//60).zfill(2)
    S = str(num%60).zfill(2)
    return H + ":" + M + ":" + S

def solution(play_time, adv_time, logs):
    answer = ''
    time_num = cvtT2N(play_time)
    adv_num = cvtT2N(adv_time)
    timeLog = [0 for _ in range(time_num+1)]

    for log in logs:
        start_t, end_t = log.split('-')
        timeLog[cvtT2N(start_t)] += 1
        timeLog[cvtT2N(end_t)] += -1
    
    for i in range(1, len(timeLog)):
        timeLog[i] = timeLog[i-1] + timeLog[i]
    
    sumM = sum(timeLog[time_num-adv_num:])
    sumMP = 0
    tmpsumM = sumM
    
    for i in range(time_num-adv_num, -1, -1):
        tmpsumM += timeLog[i] - timeLog[i + adv_num]
        if tmpsumM >= sumM:
            sumM = tmpsumM
            sumMP = i
    answer = cvtN2T(sumMP)
    return answer