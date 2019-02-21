gender = input('Gender: ')
age = input('Age: ')
age = int(age)
score = input('Score: ')
score = int(score)


def bonus(gender, age, score):
    if age < 21:
        return 0
    if gender== 'F' and age >= 21 and age <= 39:
        return 100
    if gender== 'F' and age >= 40:
        return 50
    if gender== 'M' and age >= 21 and age <= 39:
        return 50
    if gender== 'M' and age >= 40:
        return 20

def points(score):
    if score + bonus(gender, age, score) >= 500:
        return True
    else:
        return False

def ageapp(age):
    if age < 21:
        return False
    else:
        return True

def approve(gender, age, score):
    if ageapp(age)  and points(score):
        return True
    else:
        return False

result = approve(gender, age, score)
print(result)
foo = str(score + int(bonus(gender, age, score)))
print('Your score is: ' + foo)