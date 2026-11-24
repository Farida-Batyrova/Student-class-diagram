# Student Class Diagram - Python

**Name:** Farida Batyrova
**Student number:** 20253832

This project maps a Student class diagram to Python code.

## Classes

| Class | Attributes | Methods |
| --- | --- | --- |
| Student | student_id, name, email, age, gpa, enrolled_courses | enroll(), drop(), total_credits(), display_info() |
| Course | code, title, credits, students | add_student(), remove_student(), student_count() |

Relationship: a student can enroll in many courses, and a course can have many students (many-to-many association).

## Diagram to code mapping

- Class -> `class`
- Attribute -> `self.xxx` variables inside `__init__`
- Operation (method) -> functions inside the class
- Association -> a list inside a class that holds objects of the other class

## Run

```
python main.py
```
