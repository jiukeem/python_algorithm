def solution(a, b):
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    days = sum(months[:a]) + b
    return weekdays[days%7]