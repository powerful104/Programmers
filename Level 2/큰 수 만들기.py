def solution(number, k):
    answer = ""
    arr = []

    for i in number:
        while arr and arr[-1] < i and k > 0:
            k -= 1
            arr.pop()
        arr.append(i)

    return "".join(arr[:len(arr)-k])

"""
문제를 풀고도 계속 시간초과가 나서 다른사람의 풀이에서 힌트를 얻어 작성한 코드이다
아직 효율성에 대한 부분이 미숙한것 같다.
"""