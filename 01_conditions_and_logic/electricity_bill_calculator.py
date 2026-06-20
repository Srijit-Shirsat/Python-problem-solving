# Assignment 6

units_consumption=int(input("Units consumed: "))

if units_consumption < 0:
    print("INVALID INPUT")
else: 
    if units_consumption >= 0 and units_consumption <= 100:
        total_bill=(units_consumption*5)
        print("Total bill for consumption is =" ,total_bill)
        
    elif units_consumption >= 101 and units_consumption <= 200:
        total_bill=(units_consumption*7)
        print("Total bill for consumption is =" ,total_bill)
        
    elif units_consumption >= 201:
        total_bill=(units_consumption*10)
        print("Total bill for consumption is =" ,total_bill)