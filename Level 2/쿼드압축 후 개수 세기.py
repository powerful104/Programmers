arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
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
print(num1, num2)