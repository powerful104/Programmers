from datetime import datetime
import math

def calcFee(fees, minute):
    finFee = fees[1] + (max(0, math.ceil((minute - fees[0])/fees[2]))) * fees[3]
    return finFee

def calcMin(time_In, time_Out):
    time_1 = datetime.strptime(time_In,"%H:%M")
    time_2 = datetime.strptime(time_Out,"%H:%M")
    time_interval = time_2 - time_1
    minute = time_interval.seconds//60
    return minute
    
def solution(fees, records):
    cars = {}
    current = {}
    for record in records:
        time, num, IoO = record.split()
        if IoO == 'IN':
            current[num] = time
        else:
            minute = calcMin(current[num], time)
            del(current[num])
            cars[num] += minute
        if num not in cars:
            cars[num] = 0
            
    for i in current.keys():
        minute = calcMin(current[i], '23:59')
        cars[i] += minute
        
    car_num = sorted(list(cars.keys()))
    answer = []
    
    for i in car_num:
        answer.append(int(calcFee(fees, cars[i])))
    return answer

    """
    어려운 문제는 아니었다.
    """