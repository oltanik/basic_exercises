# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
count_student = {}
for student_dict in students:
    for key, name in student_dict.items():
        if name in count_student:
            count_student[name] += 1
        else:
            count_student[name] = 1
for name, count in count_student.items():
    print(f'{name}: {count}')



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
counter_student_name_max = {}
for students_dict in students:
    for key, name in students_dict.items():
        if name in counter_student_name_max:
            counter_student_name_max[name] += 1
        else:
            counter_student_name_max[name] = 1
name = sorted(counter_student_name_max.items(), key=lambda item: item[1], reverse=True)
print(f'Самое частое имя среди учеников: {name[0][0]}')

# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

def max_count_name(arg, arg2):
    counter_student_name_max = {}
    for students_dict in arg:
        for key, name in students_dict.items():
            if name in counter_student_name_max:
                counter_student_name_max[name] += 1
            else:
                counter_student_name_max[name] = 1
    name_student = sorted(counter_student_name_max.items(), key=lambda item: item[1], reverse=True)
    
    return f'Самое частое имя в классе  {arg2}: {name_student[0][0]}'
    

number_class = 0
for school_class in school_students:
    number_class += 1
    print(max_count_name(school_class, number_class))


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

def student_counting(val, numb):
    counter_gender_student = {'men': 0, 'female': 0}
    for student_dict in val:
        for key, name in student_dict.items():
            if is_male[name] is True:
                counter_gender_student['men'] += 1
            else:
                counter_gender_student['female'] += 1
    return f'Класс {numb}: девочки {counter_gender_student["female"]}, мальчики {counter_gender_student["men"]}'



for classes in school:
    for key, value in classes.items():
        if type(value) is type(list()):
            value_list = value
        else:
            number_class = value
    print(student_counting(value_list, number_class))


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
def student_counting(val, numb):
    counter_gender_student = {'men': 0, 'female': 0}
    for student_dict in val:
        for key, name in student_dict.items():
            if is_male[name] is True:
                counter_gender_student['men'] += 1
            else:
                counter_gender_student['female'] += 1
    if counter_gender_student['men'] > counter_gender_student['female']:
        return f'Больше всего мальчиков в классе {numb}'
    else:
        return f'Больше всего девочек в классе {numb}'



for classes in school:
    for key, value in classes.items():
        if type(value) is type(list()):
            value_list = value
        else:
            number_class = value
    print(student_counting(value_list, number_class))

