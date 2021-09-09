def solution(numbers):
    answer = []
    for num in numbers:
        b = bin(num)[:2] + '0' + bin(num)[2:]
        for i in range(len(b)-1,-1,-1):
            if b[i] == '0':
                b = b[:i]+"1"+b[i+1:]
                if i != len(b)-1:
                    b= b[:i+1]+"0"+b[i+2:]
                break
        answer.append(int(b,2))
    return answer

"""
가장 뒤에 있는 0을 1로 바꿔주고 만약 그자리가 가장 끝자리가 아니라면 바로 뒤에 있는 1을 0으로 바꿔주면
비트의 개수가 1~2개 차이나는 수중에 가장 작은 수가 나온다
따라서 해당 과정을 코드로만 바꿔주었다

어떤 사람은 논리식을 이용하여 5줄정도에 푼사람도 있었다
신기한 코드다
def solution(numbers):
    answer = []
    for idx, val in enumerate(numbers):
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer
"""