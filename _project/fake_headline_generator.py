import random

subjects = [
    "Shah Rukh Khan",
    "Aamir Khan",
    "Salman Khan",
    "A Mumbai Cat",
    "An Alien from Mars",
    "A Group of Monkeys",
    "Auto Rickshaw Driver from delhi"
]

actions =[
    "launches",
    "cancels",
    "dance",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things = [
    "at Taj Hotel",
    "in Mumbai Local Train",
    "a plate of samosa",
    "at india gate",
    "during IPL Match",
    "inside parliament",
    "at big boss house"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {places}"
    print("\n"+ headline)

    user_input = input("\nDo you want another headline? (yes/no): ").strip().lower() #strip - remove spaces from both sides
    if user_input == 'no':
        break

print("\nThanks for using the Fake News Headline Generator. Have a fun day")