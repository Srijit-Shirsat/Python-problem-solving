#ASsignment 7

performance_score=int(input("Enter the score: "))
years_of_service=int(input("Years served: "))

if performance_score < 0 or performance_score > 100:
    print("INVALID INPUTS: Score must be between 0-100")
elif years_of_service < 0:
    print("INVALID INPUT: Years cannot be negative")
else:
    if performance_score >= 90 and years_of_service >= 5:
        print("GOLD BONUS")
    elif performance_score >=75 and years_of_service >=3:
        print("SILVER BONUS")
    elif performance_score >=60 and years_of_service >=1:
        print("BRONZE BONUS")
        
    else:
        print("NO BONUS")