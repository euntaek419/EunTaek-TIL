function solution(a, b) {
    specificDate = new Date(2016, a - 1, b);
    weekday = specificDate.getDay();
    
    weekdayName = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    
    return weekdayName[weekday];
}