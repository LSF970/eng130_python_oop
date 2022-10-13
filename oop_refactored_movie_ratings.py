# Film rating - Refactored using a function
# Not using classes and objects

film_rating = input("Enter your age")


def movie_rating(age):
    if film_rating.lower() == "universal":
        print("all age groups can watch this film")
    elif film_rating.lower() == "pg":
        print("General viewing, but some scenes may be unsuitable for young children.")
    elif film_rating.lower() == "12" or film_rating == "12a":
        print("Films classified 12A and video works classified 12 contain material that is not generally suitable for children aged under 12. No one younger than 12 may see a 12A film in a cinema unless accompanied by an adult.")
    elif film_rating.lower() == "15":
        print("No one younger than 15 may see a 15 film in a cinema.")
    elif film_rating.lower() == "18":
        print("No one younger than 18 may see an 18 film in a cinema.")
    else:
        print("this is not a correct rating, please use universal, pg, 12, 12a, 15, 18")
    return f"Your age is  {age}"

print(movie_rating(film_rating))

