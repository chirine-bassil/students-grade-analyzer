def display_student_summary(students, grades):
    print("\nthe students in this class are ")
    for i in range(len(students)):
        student = students[i]
        grade = grades[i]
        print(f"Name: {student}, Grade: {grade}")




def get_avg_grade(grades):
    if len(grades) == 0:
        return 0
    return sum(grades) / len(grades)

def get_highest_grade(students, grades):
    if not grades:
        return []

    max_grade = max(grades)
    top_students = [
        (students[i], grades[i])
        for i in range(len(grades))
        if grades[i] == max_grade
    ]

    # fi possibilite ykoun plusieurs students have the same higher grade
    return top_students


def count_passed(grades):
    count = 0
    for grade in grades:
        if grade >= 60:
            count += 1
    return count


def main():
    num_students = int(input("how many student in the class: "))
    students = []
    grades = []

    for _ in range(num_students):
        name = input("student's name: ")
        while True:
            try:
                grade = float(input(f" {name} grade (/100): "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("the grade should be out of 100.")
     #li2an ma fina nhout 2 else taht l if     - lezim ywa2ef iza fi possiblite ghaalt mich nb          
            except ValueError:
                print(" Please entre the value.")
        
        students.append(name)
        grades.append(grade)

    display_student_summary(students, grades)
    
    avg_grade = get_avg_grade(grades)
    print(f"\nthe average grade of the class: {avg_grade:.2f}")

    top_students = get_highest_grade(students, grades)
    if top_students:
        print("the highest grade earned by:")
        for student, grade in top_students:
            print(f" - {student} with a grade of {grade}")
    else:
        print("There is no student ")

    passed_count = count_passed(grades)
    print(f"the count of students who passed (grade >= 60): {passed_count}")

if __name__ == "__main__":
    main()