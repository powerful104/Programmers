def solution(phone_book):
    sig = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].find(phone_book[i]) == 0:
            sig = False
            break
    return sig

"""
처음에는 이중포문으로 진행하였더니 역시 효율성 테스트에서 시간초과가 뜨고 말았다.
따라서 어자피 접두어로 포함되는 문자열을 바로옆에 정렬될테니
이웃한 요소들만 비교를 해주는 식으로 바꾸었다.
"""