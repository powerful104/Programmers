def solution(numbers, hand):
    num = ["1","2","3","4","5","6","7","8","9","*","0","#",]
    answer = ""
    curL = "*"
    curR = "#"
    for i in numbers:
        if i%3 == 1:
            answer += "L"
            curL = str(i)
        elif i%3 == 0 and i != 0:
            answer += "R"
            curR = str(i)
        else:
            distL = abs(num.index(str(curL))//3 - num.index(str(i))//3) + abs(num.index(str(curL))%3 - num.index(str(i))%3)
            distR = abs(num.index(str(curR))//3 - num.index(str(i))//3) + abs(num.index(str(curR))%3 - num.index(str(i))%3)
            if distL < distR:
                answer += "L"
                curL = str(i)
            elif distL > distR:
                answer += "R"
                curR = str(i)
            else:
                if hand[0] == "l":
                    answer += "L"
                    curL = str(i)
                else:
                    answer += "R"
                    curR = str(i)
    return answer
"""
구현하는 문제였다.
"""