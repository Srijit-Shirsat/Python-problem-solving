# Assignment 3

score = int(input("Enter the score: "))

if score < 0 or score > 100:
    print("invalid score cannot be evaluated")
elif score >= 0 and score <= 49:
    print("Poor")
elif score >= 50 and score <= 69:
    print("Average")
elif score >= 70 and score <= 89:
    print("Good")
elif score >= 90 and score <= 100:
    print("Outstanding")