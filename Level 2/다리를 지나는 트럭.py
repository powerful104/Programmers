def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length
    answer = 0
    while len(truck_weights) != 0 or sum(bridge) != 0:
        del bridge[0]
        if len(truck_weights) == 0 or sum(bridge) + truck_weights[0] > weight:
            bridge.append(0)
        else:
            bridge.append(truck_weights[0])
            del truck_weights[0]
        answer += 1
    return answer

"""
깊이 생각안하고 간단하게 풀어보고 싶어서 큐를 사용했다
큐에 순서대로 넣고 1초에 하나씩 앞에것을 삭제,및 기준에 맞을시 뒤에도 넣는 식으로 구현
시간을 많이 먹는 케이스가 있었긴하다
"""