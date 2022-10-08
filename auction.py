from replit import clear
from images import painting
from art import logo

biddings = {}
print("Welcome to the auction for The Hag and the Young Woman by Normand Veilleux!\n")
print(painting)

number_of_people = True
while number_of_people:
    name = input("What is your name? ")
    bid = int(input("What is your bid in dollars? "))
    biddings[name] = bid
    remaining_people = input("Do you see any more people? yes or no? ")
    
    if remaining_people == "no":
        number_of_people = False

    if remaining_people == "yes":
        print(painting)
        clear()


for i in biddings:
    value = 0
    person_who_won = ""
    if biddings[i] >= value:
        value = biddings[i]
        person_who_won = i
        

print(logo)
print(f"Sold! The winner is {i} with a winning bid of ${value}!!")
    

    
        