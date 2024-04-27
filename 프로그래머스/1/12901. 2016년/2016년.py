import datetime

def solution(a, b):
    specific_date = datetime.date(2016, a, b)
    weekday = specific_date.weekday()
    
    weekday_name = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    
    return weekday_name[weekday]