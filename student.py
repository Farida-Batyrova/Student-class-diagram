"""Student class diagram mapped to Python.

Author: Farida Batyrova
Student number: 20253832
"""


class Course:
    """Represents a course (the Course class in the diagram)."""

    def __init__(self, code, title, credits):
        self.code = code
        self.title = title
        self.credits = credits
        self.students = []  # Students enrolled in this course

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def student_count(self):
        return len(self.students)


class Student:
    """Represents a student (the Student class in the diagram)."""

    def __init__(self, student_id, name, email, age):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.age = age
        self.gpa = 0.0
        self.enrolled_courses = []  # Courses the student is taking

    def enroll(self, course):
        """Enroll the student in a course."""
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            course.add_student(self)

    def drop(self, course):
        """Remove the student from a course."""
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            course.remove_student(self)

    def total_credits(self):
        """Calculate the total credits of the student's courses."""
        return sum(course.credits for course in self.enrolled_courses)

    def display_info(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"GPA: {self.gpa}")
        print(f"Total credits: {self.total_credits()}")
        print("Courses:")
        for course in self.enrolled_courses:
            print(f"  - {course.code} {course.title}")
