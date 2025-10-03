def find_shortest_name_student(students: list) -> str:
    student_name = max(students , key = lambda student: len(student['name']))
    return student_name['name']
students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]
print(find_shortest_name_student(students))