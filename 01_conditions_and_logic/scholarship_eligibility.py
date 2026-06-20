#Assignment 5

student_marks=int(input("Enter marks of student: "))
attendance=int(input("Enter attendance: "))

if student_marks < 0 or student_marks > 100 or attendance < 0 or attendance > 100:
    print("INAVLID INPUT")
elif student_marks >= 80 and student_marks <=100 and attendance >= 75 and attendance <=100:
    print ("SCHOLARSHIP APPROVED")
else:
    print("SCHOLARSHIP DENIED") 