def calculate_avg_grade(students):
    for k,v in students.items():
        print(f"{k} has an average grade of {sum(v)/len(v)}")

def highest_grade(students):
    good_student = None
    good_avg = 0

    for student, grades in students.items():
        avg_grade = sum(grades) / len(grades)
        if avg_grade > good_avg:
            good_avg = avg_grade
            good_student = student

    print(f"Student with the highest average grade: {good_student} ({good_avg:.2f})")

def passed_students(students):
    passed = {k: sum(v) / len(v) for k, v in students.items() if (sum(v) / len(v)) >= 50}
    print(f"Number of students who passed: {len(passed)}")



students = {"dhoni":[85, 90, 78, 92],
            "raina":[60, 65, 70, 75],
            "jaddu":[40, 45, 50, 55],
            "rachin":[95, 100, 98, 92]}
calculate_avg_grade(students)
highest_grade(students)
passed_students(students)