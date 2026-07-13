# Assignment 9

age=int(input("Enter your age: "))
monthly_income=int(input("What is your monthly income: "))
credit_score=int(input("Your credit score: "))
existing_loan=input("Do you have existing loan(YES/NO): ")

if age < 0 or age > 100:
    print("INVALID AGE")
elif monthly_income < 0:
    print("INCOME CANNOT BE NEGATIVE")
elif credit_score < 300 or credit_score > 900:
    print ("INVALID CREDIT SCORE")
elif existing_loan != "YES" and existing_loan != "NO":
    print("INVALID INPUT")
    
elif age >= 21 and monthly_income >= 50000 and credit_score >= 450 and existing_loan == "NO":
    print ("LOAN APPROVED")
elif (
    ( 
        age < 21 
        and monthly_income >= 50000
        and credit_score >= 450
        and existing_loan == "NO" 
    )
    or 
    (
        age > 21
        and monthly_income < 50000
        and credit_score >= 450 
        and existing_loan == "NO"    
    )
    or
    (
        age > 21
        and monthly_income >= 50000
        and credit_score <= 450
        and existing_loan == "NO"    
    )
    or
    (
        age > 21
        and monthly_income >= 50000
        and credit_score >= 450
        and existing_loan == "YES"    
    )
):
    print("LOAN UNDER REVIEW")
    
elif (
    (
        credit_score <= 350 and existing_loan == "YES"
    )
):
    print ("LOAN REJECTED")
    
else:
    print ("LOAN NOT APPLICABLE")
    
    

    