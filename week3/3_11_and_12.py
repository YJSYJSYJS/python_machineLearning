# 3-11 & 3-12

year = int(input("What year? "))
month = int(input("What month? "))
days=[31,31,30,31,30,31,31,30,31,30,31]

def is_leap(y):
    """
    입력받은 년도 y가 윤년인지 아닌지 판별하고
    days의 2월 자리에 해당 날짜 수를 삽입한다.
    """
    if y%4==0:
        if y%100!=0:
            days.insert(1, 29)
            return True
        elif y%400==0:
            days.insert(1, 29)
            return True
    else:
        days.insert(1, 28)
        return False
    
if is_leap(year):
    print(year, "년은 윤년입니다.")
else:
    print(year, "년은 윤년이 아닙니다.")

print("{}년 {}월은 {}일".format(year, month, days[month-1]))


