import re
def solution(expression):
    num = re.split('[-+*]',expression)
    ex = ' '.join(re.split('[0123456789]',expression)).split()
    case = ["-+*", "-*+", "+-*", "+*-", "*-+", "*+-"]
    mx = 0
    for i in case:
        tmpnum = list(num)
        tmpex = list(ex)
        for exp in i:
            j = 0
            while j < len(tmpex):
                if tmpex[j] == exp:
                    num1 = tmpnum[j]
                    num2 = tmpnum[j+1]
                    del tmpnum[j+1]
                    del tmpnum[j]
                    tmpnum.insert(j,str(eval(num1+exp+num2)))
                    del tmpex[j]
                else:
                    j += 1
        if abs(int(tmpnum[0])) > mx:
            mx = abs(int(tmpnum[0]))
    return mx

"""
먼저 수와 연산자로 구분지어 나누고
각 연산자의 우선순위가 들어있는 리스트를 반복시켜서 해당 우선순위로 계산을 하게끔 하여 풀었다.
우선순위에 해당하는 연산자와 같은 연산자가 있는지 확인후 있다면 계산후 숫자 리스트에서 계산한 수와 연산자는 제거하고 새로운 수를
추가하는 방식으로 구현
"""