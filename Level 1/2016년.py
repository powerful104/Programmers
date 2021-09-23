import datetime
def solution(a, b):
    week = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return(week[datetime.datetime(2016,a,b).weekday()])

"""
datetime 모듈을 이용하였다.
"""