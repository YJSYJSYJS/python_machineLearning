# 90이상 A, 80이상 B, 70 C, 60 D, F, 입력: 점수, 리턴: 학점

score = int(input("당신의 점수는? "))

def grading(sc):
    if sc>=90:
        return 'A'
    elif sc>=80:
        return 'B'
    elif sc>=70:
        return 'C'
    elif sc>=60:
        return 'D'
    else:
        return 'F'


print("{}점은 {}입니다".format(score, grading(score)))