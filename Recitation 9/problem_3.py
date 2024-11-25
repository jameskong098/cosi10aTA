
def read_courses(file_path):
    with open(file_path, 'r') as file:
        courses = {}

        lines = file.readlines()
        for line in lines:
            # Get rid of the newline character and split the line by tabs
            line = line.strip().split('\t')
            # Unpack the line into variables (line is a list of strings where each string is a column in the file)
            department, course_num, section, title, format, instructor, semester, code, num_enrolled = line

            # Check if each key exists in the dictionary, if not, create it and set it to an empty dictionary
            if semester not in courses:
                courses[semester] = {}
            if department not in courses[semester]:
                courses[semester][department] = {}
            if course_num not in courses[semester][department]:
                courses[semester][department][course_num] = {}

            # By now, we know that the semester, department, and course_num keys exist in the dictionary so we can add the section key
            courses[semester][department][course_num][section] = {
                'name': title,
                'format': format,
                'instructor': instructor,
                'code': code,
                'num_enrolled': num_enrolled
            }

    return courses

def main():
    file_path = 'R9_courses_2014-19.tsv'
    courses = read_courses(file_path)

    while True:
        department = input("\nEnter the name of the department: ")
        semester = input("Enter the semester: ")

        # Get the courses for the given department and semester
        found_courses = courses[semester][department]
        print(f"\nThere are {len(found_courses)} {department} courses in {semester}.\n")
        # Loop through the courses and print them
        for course in found_courses:
            print(course)

        course_num = input("\nSelect a course: ")
        # Loop through the sections of the selected course and print them
        for section_num in found_courses[course_num]:
            # Get the current section using section_num as the key (as section_num only represents the section number not the actual section dictionary)
            cur_section = found_courses[course_num][section_num]
            print(f"\n{department} {course_num} - {section_num}")
            print(f"Name: {cur_section['name']}, Type: {cur_section['format']}, Instructor: {cur_section['instructor']}, Students: {cur_section['num_enrolled']}\n")
        
        continue_search = input('Type "stop" to stop searching, otherwise hit enter: ')
        if continue_search == 'stop':
            break 

main()
