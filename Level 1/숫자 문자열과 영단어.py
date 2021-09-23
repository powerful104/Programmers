def solution(s):
    numbers = ("zero","one","two","three","four","five","six","seven","eight","nine")
    for i in range(10):
        s = s.replace(numbers[i],str(i))
    return int(s)

"""
replace 함수를 통해 바꿔주기만 하면 되는 문제였다.
"""