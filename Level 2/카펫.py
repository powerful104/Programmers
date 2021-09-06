import math 
def solution(brown, yellow):
    b = (brown+4 - math.sqrt((brown+4)**2-16*(brown+yellow)))//4
    a = (brown+yellow)//b
    answer = [int(a),int(b)]
    return answer