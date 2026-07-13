# Assignment 8

performance_score = int(input("Enter the employee performance score: "))
attendance_percentage = int(input("Enter attendance percentage: "))
years_of_experience = int(input("Enter employee's total years of experience: "))
disciplinary_action = input("Disciplinary action (YES/NO): ")


if performance_score < 0 or performance_score > 100:
    print("INVALID PERFORMANCE SCORE")

elif years_of_experience < 0:
    print("INVALID EXPERIENCE")

elif attendance_percentage < 0 or attendance_percentage > 100:
    print("INVALID ATTENDANCE")

elif disciplinary_action != "YES" and disciplinary_action != "NO":
    print("INVALID DISCIPLINARY STATUS")

elif (
    performance_score >= 90
    and years_of_experience >= 5
    and attendance_percentage >= 95
    and disciplinary_action == "NO"
):
    print("PROMOTION APPROVED")

elif (
    (
        performance_score < 90
        and years_of_experience >= 5
        and attendance_percentage >= 95
        and disciplinary_action == "NO"
    )
    or
    (
        performance_score >= 90
        and years_of_experience < 5
        and attendance_percentage >= 95
        and disciplinary_action == "NO"
    )
    or
    (
        performance_score >= 90
        and years_of_experience >= 5
        and attendance_percentage < 95
        and disciplinary_action == "NO"
    )
    or
    (
        performance_score >= 90
        and years_of_experience >= 5
        and attendance_percentage >= 95
        and disciplinary_action == "YES"
    )
):
    print("PROMOTION UNDER REVIEW")

elif disciplinary_action == "YES":
    print("PROMOTION REJECTED")

else:
    print("NO PROMOTION")