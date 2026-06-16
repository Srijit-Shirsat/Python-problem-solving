#Assignment 1

age = int(input("Enter your age: "))
employee_id=(input("Enter your ID: "))
training_completed=input("Enter your training status(completed or not completed): ")

if age < 21 :
    print("Access denied: UNDERAGE")
elif employee_id.isalpha() == True: 
    print ("Access denied : Invalid ID should be integer")
elif int(employee_id) < 0:
    print ("Access denied : Invalid ID cannot be negative")
elif training_completed == "not completed":
    print("Access denied : Training not completed")
else:
    print ("Access granted")