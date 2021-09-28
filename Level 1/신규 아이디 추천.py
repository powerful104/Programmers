def solution(new_id):
    poss = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
        "0","1","2","3","4","5","6","7","8","9",
        "-","_","."]

    invalid = False
    if (not 3 <= len(new_id) <= 15) or new_id[0] == '.' or new_id[-1] == '.' or new_id.count("..") > 0:
        invalid = True
    for i in new_id:
        if not i in poss:
            invalid = True
    
    tmpnew = ''
    if invalid:
        #1단계
        new_id = new_id.lower()

        #2단계
        for i in new_id:
            if i in poss:
                tmpnew += i

        #3단계
        while tmpnew.count("..") != 0:
            tmpnew = tmpnew.replace("..",".")

        #4단계
        if len(tmpnew) != 0 and tmpnew[0] == ".":
            tmpnew = tmpnew[1:]
        if len(tmpnew) != 0 and tmpnew[-1] == ".":
            tmpnew = tmpnew[:-1]

        #5단계
        if len(tmpnew) == 0:
            tmpnew = "a"
        
        #6단계
        if len(tmpnew) >= 16:
            tmpnew = tmpnew[:15]
            if tmpnew[-1] == ".":
                tmpnew = tmpnew[:-1]
        
        #7단계
        if len(tmpnew) <= 2:
            while len(tmpnew) !=3:
                tmpnew += tmpnew[-1]
    else:
        return new_id
    return tmpnew

"""
단계를 나누어 풀이하였다.
정규식을 이용해 간단하게 풀이한 사람도 있었다.
"""