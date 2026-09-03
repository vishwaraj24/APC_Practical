from student_info import Student, Exam
name = input("Enter Student Name: ")
roll_no = input("Enter Roll No: ")
class_name = input("Enter Class: ")
mobile_no = input("Enter Mobile No: ")

student = Student(name, roll_no, class_name, mobile_no)

marks = []

for i in range(1, 5):
    mark = float(input("Enter marks for Semester " + str(i) + ": "))
    marks.append(mark)

exam = Exam(marks)

student.display_student_info()
exam.display_exam_info()
