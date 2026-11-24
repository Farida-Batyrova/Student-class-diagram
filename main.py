"""Example usage of the Student and Course classes.

Author: Farida Batyrova
Student number: 20253832
"""

from student import Student, Course


def main():
    student = Student(20253832, "Farida Batyrova", "farida@example.com", 21)
    student.gpa = 3.4

    oop = Course("SE201", "Object Oriented Programming", 4)
    db = Course("SE305", "Database Systems", 3)

    student.enroll(oop)
    student.enroll(db)

    print("--- After enrollment ---")
    student.display_info()

    student.drop(db)

    print()
    print("--- After dropping Database Systems ---")
    student.display_info()
    print("Students in SE201:", oop.student_count())


if __name__ == "__main__":
    main()
