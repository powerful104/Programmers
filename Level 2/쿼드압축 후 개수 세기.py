cnt0 = 0
cnt1 = 0

def calc(size,arr):
    global cnt0
    global cnt1
    if size == 1 :
        if arr[0][0] == 0:
            cnt0 += 1
            return
        elif arr[0][0] == 1:
            cnt1 += 1
            return
    check = 0
    for i in range(size):
        for j in range(size):
            if arr[i][j] == arr[0][0]:
                check += 1
    if check != size**2:
        calc(size//2, [arr[i][:size//2] for i in range(size//2)])
        calc(size//2, [arr[i][size//2:] for i in range(size//2)])
        calc(size//2, [arr[i][:size//2] for i in range(size//2,size)])
        calc(size//2, [arr[i][size//2:] for i in range(size//2,size)])
    elif arr[0][0] == 0:
        cnt0 += 1
    elif arr[0][0] == 1:
        cnt1 += 1
        
def solution(arr):
    calc(len(arr),arr)
    return [cnt0, cnt1]

"""
정말 귀찮은 문제였다.
내사 처음에 풀려던 방식은 DP와 비슷하게 만들수있는 사각형을 계속해서 수를 저장시키며 비교하는것이었는데
이게 도대체 왜 틀린지 모르겠다.
그래서 힌트를 얻어 재귀로 풀긴했지만 내 알고리즘이 왜 틀렸었는지 도저히 알 수가 없다.
밑에는 원래 내가 적었던 코드이다.

def solution(arr):
    size = 2
    for i in range(len(arr)):
        tmp = []
        for j in arr[0]:
            if j == 1:
                tmp.append(1)
            else:
                tmp.append(-1)
        del arr[0]
        arr.append(tmp)
    while size <= len(arr):
        for r in range(size-1,len(arr),size):
            for c in range(size-1, len(arr[0]),size):
                if arr[r][c] == arr[r][c-size//2] == arr[r-size//2][c] == arr[r-size//2][c-size//2] != 0:
                    arr[r][c-size//2] = 0
                    arr[r-size//2][c] = 0
                    arr[r-size//2][c-size//2] = 0
                    if arr[r][c] < 0:
                        arr[r][c] -= 1
                    else:
                        arr[r][c] += 1
        size *= 2
    new = sum(arr,[])
    num1 = 0
    num2 = 0
    for i in new:
        if i<0:
            num1 += 1
        elif i>0:
            num2 += 1
    return [num1, num2]
"""