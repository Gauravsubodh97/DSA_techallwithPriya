exam_score =[77,76,82,33,55]

def grade(exam_score):
    if exam_score >=90:
         return 'A'
    elif exam_score <90 and exam_score >=80:
        return 'B'
    elif exam_score < 80 and exam_score >=70:
        return 'C'
    elif exam_score <70 and exam_score >=60:
        return "D"
    else:
        return 'F'

result = list(map(grade,exam_score))
print(exam_score,result)
