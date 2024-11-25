# Example of nested dictionaries

students = {
    'student1': {
        'name': 'John Doe',
        'age': 21,
        'courses': {
            'course1': 'Math',
            'course2': 'Science'
        }
    },
    'student2': {
        'name': 'Jane Smith',
        'age': 22,
        'courses': {
            'course1': 'English',
            'course2': 'History'
        }
    }
}

# Accessing nested dictionary values
print(students['student1']['name'])  # Output: John Doe
print(students['student2']['courses']['course2'])  # Output: History

print(students.keys())  # Output: dict_keys(['student1', 'student2'])
print(students['student1'].keys())  # Output: dict_keys(['name', 'age', 'courses'])


list_1 = [[1, 2, 3], [6, 7, 8]]
print(list_1[0][2])  # Output: 3


