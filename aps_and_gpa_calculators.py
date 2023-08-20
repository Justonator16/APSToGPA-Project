
def APSLevel(grade):
        if grade >= 0 and grade <= 29:
            return 1
        elif grade >= 30 and grade <= 39:
            return 2
        elif grade >= 40 and grade <= 49:
            return 3
        elif grade >= 50 and grade <= 59:
            return 4
        elif grade >= 60 and grade <= 69:
            return 5
        elif grade >= 70 and grade <= 79:
            return 6
        else:
            return 7

def GradeToLetter(grade):
    if grade >= 0 and grade < 60:
        return "F"
    elif grade >= 65 and grade <= 66:
        return "D"
    elif grade >= 67 and grade <= 69:
        return "D+"
    elif grade >= 70 and grade <= 72:
        return "C-"
    elif grade >= 73 and grade <= 76:
        return "C"
    elif grade >= 77 and grade <= 79:
        return "C+"
    elif grade >= 80 and grade <= 82:
        return "B-"
    elif grade >= 83 and grade <= 86:
        return "B"
    elif grade >= 87 and grade <= 89:
        return "B+"
    elif grade >= 90 and grade <= 92:
        return "A-"
    elif grade >= 93 and grade <= 96:
        return "A"
    else:
        return "A+"

def GradeToGpaScale(grade):
    if grade >= 0 and grade < 60:
        return 0.0
    elif grade >= 65 and grade <= 66:
        return 1.0
    elif grade >= 67 and grade <= 69:
        return 1.3
    elif grade >= 70 and grade <= 72:
        return 1.7
    elif grade >= 73 and grade <= 76:
        return 2.0
    elif grade >= 77 and grade <= 79:
        return 2.3
    elif grade >= 80 and grade <= 82:
        return 2.7
    elif grade >= 83 and grade <= 86:
        return 3.0
    elif grade >= 87 and grade <= 89:
        return 3.3
    elif grade >= 90 and grade <= 92:
        return 3.7
    else:
        return 4.0


