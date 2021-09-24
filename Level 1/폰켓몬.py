def solution(nums):
    answer = len(set(nums)) if len(set(nums))<=len(nums)//2 else len(nums)//2
    return answer

"""
답은 항상 nums의 개수보다 크지않은 종류의 개수만큼 나온다.
따라서 삼항연산자와 비슷한 기능을 하게끔 하였다.
"""