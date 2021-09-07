import math
def solution(w,h):
    if w < h:
        w,h = h,w
    
    GCD = math.gcd(w,h)
    newW = w//GCD
    newH = h//GCD
    prv = 0
    nexta = 0
    block = 0
    for i in range(newH):
        nexta += newW
        block += math.floor(nexta/newH)-math.floor(prv/newH)
        if nexta%newH != 0:
            block += 1
        prv += newW
    answer = w*h-block*GCD
    return answer

"""
문제를 보자마자 한칸 높이의 블럭에서 제외해야할 블럭을 하나씩 세어나가는게 좋겠다는 생각이 들었다
하지만 그대로 진행하였더니 시간초과가 떴다

원인은 높이와 너비가 큰수로 지정되어 그런것 같아서
먼저 높이와 너비의 최대공약수를 구하여
나누어 더 작은수로 구하도록 했다

import math
def solution(w,h):
    GCD = math.gcd(w,h)
    newW = w//GCD
    newH = h//GCD
    prv = 0
    nexta = 0
    block = 0
    for i in range(newH):
        nexta += newW
        block += math.floor(nexta/newH)-math.floor(prv/newH)
        if nexta%newH != 0:
            block += 1
        prv += newW
    answer = w*h-block*GCD
    return answer

이와 같은 코드를 작성하였더니 몇몇개는 시간초과를 통과하였지만 3개의 케이스가 통과가 되지 않았다.
아무래도 큰소수와 큰소수로 이루어진 케이스 인것 같다는 생각이 들었다

이후에 새롭게 생각을 해봤다
높이와 너비가 큰 차이가 있을때 높이만으로 나누어 판단하면 더 느릴것같다
따라서
if w < h:
    w,h = h,w
코드를 넣어 더 작은 값이 높이로 들어가게끔 하였더니
시간초과는 통과되었다

하지만 정확하지는 않은것 같고 다른방법이 있을것 같다

+ 다른 사람의 풀이를 확인했더니

def gcd(a,b): return b if (a==0) else gcd(b%a,a)    
def solution(w,h): return w*h-w-h+gcd(w,h)

이와 같은 해답이 있었다
나 역시 그림을 그려보며 이문제는 최대공약수와 관련이 있을것 같다는 생각이 들었었는데
더 세세하게 분석하지 못한것 같다
"""