# Assignment 2

age = int(input("Enter your age: "))
movie_rating = input("Enter the movie rating: ")

if movie_rating != "U" and movie_rating != "UA" and movie_rating != "A": 
    print("Invalid rating")
elif movie_rating == "A" and age < 18 or movie_rating == "UA" and age < 13:
    print("ENTRY DENIED: TOO YOUNG") 
else:
    print ("ENTRY ALLOWED")