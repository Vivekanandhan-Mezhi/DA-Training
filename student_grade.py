# Student Grade Management
# Scenario: You are developing a student grade management system for a school.
#  Each student has a unique ID and a list of courses they are enrolled in, along with their grades 
# in each course. You need to calculate the GPA for each student and identify the student with the 
# highest GPA.

# Question: Write a function that takes a dictionary representing the students 
# (student IDs as keys and a dictionary of courses and grades as values) and returns a dictionary 
# of GPAs for each student and the student ID with the highest GPA.

student_details = {1001: {"science": 50, "Math": 78, "Social Science": 77, "English": 78, "Tamil": 89},
                   1002: {"science": 95, "Math": 100, "Social Science": 96, "English": 95, "Tamil": 91},
                   1003: {"science": 70, "Math": 87, "Social Science": 78, "English": 67, "Tamil": 78},
                   1004: {"science": 90, "Math": 98, "Social Science": 93, "English": 96, "Tamil": 95}}

def highest_score(student_details):
    student_marks = {}
    stu_id = 0
    highest_gpa = float('-inf')
    for key, value in student_details.items():
        marks = 0
        # value.values - gives value in dict, value.key - gives key of dict
        for _, mark in value.items():
            marks+=mark
        marks=marks/len(value)
        if marks > highest_gpa:
            highest_gpa = marks
            stu_id = key
        student_marks[key]=marks
    return student_marks, (stu_id, highest_gpa)

print(highest_score(student_details))