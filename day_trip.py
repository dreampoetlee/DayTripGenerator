import random

# Trip Greeting Message
greeting_message = 'Thank you for using our Day Trip Generator to plan your upcoming day excursion.'

# Lists Code Block
# Created destination list and randomily selected destination
trip_destinations = ['Provincetown, MA', 'Fort Lauderdale, FL', 'San Juan, PR', 'Fire Island, NY', 'Palm Springs, CA', 'Honolul, HI']
# Created destination list and randomily selected restaurants 
best_restaurants = ['Crown & Anchor Restaurant', 'Heritage', 'Oasis Tapas & Lounge', 'The Blue Whale', 'Hunters Palm Springs', 'Bacchus Waikiki']
# Created destination list and randomily selected mode of transportation
best_transportations = ['walking', 'the electric bike', 'the bus', 'the train', 'a yacht', 'a helicopter']
# Created destination list and randomily selected entertainment 
best_entertainments = ['walking tours', 'segway tours', 'bus tours', 'cooking classes', 'amusement parks', 'theater']

# Selected Options
destination = random.choice(trip_destinations)
restaurant = random.choice(best_restaurants)
transportation = random.choice(best_transportations)
entertainment = random.choice(best_entertainments)

# Day Trip Greeting
day_trip = (f' For your trip, we have selected {destination} for your destination, {restaurant} as the best place to eat, {transportation} as the best way to travel around town, and {entertainment} as a fun activity for the day. Do you like our choices? ')

print(greeting_message + day_trip)

confirm_choice = input('Please enter y/n to confirm these travel options. ')

# Function for new destination
def new_dest(confirm_choice):  
  while confirm_choice != 'y':
    destination = random.choice(trip_destinations)
    confirm_choice = input(f'We are sorry that the previous option did not work for your. We have seleceted {destination} as another trip destination. Does this work for you? ')
  else:
    print(f'You have selected {destination} as the destination for your trip. ')

new_dest(confirm_choice)

# Function for new restaurant
def new_restaurant(confirm_choice):  
  while confirm_choice != 'y':
    restaurant = random.choice(best_restaurants)
    confirm_choice = input(f'We are sorry that the previous option did not work for your. We have seleceted {restaurant} as another place to eat. Does this work for you? ')
  else:
    print(f'You have selected {restaurant} as the best place to eat during your trip. ')

new_restaurant(confirm_choice)

# Function for new transportation
def new_trans(confirm_choice):  
  while confirm_choice != 'y':
    transportation = random.choice(best_transportations)
    confirm_choice = input(f'We are sorry that the previous option did not work for your. We have seleceted {transportation} as the best way to travel. Does this work for you? ')
  else:
    print(f'You have selected {transportation} as a way to get around. ')

new_trans(confirm_choice)

# Function for new entertaiment
def new_entertainment(confirm_choice):  
  while confirm_choice != 'y':
    entertainment = random.choice(best_entertainments)
    confirm_choice = input(f'We are sorry that the previous option did not work for your. We have seleceted {entertainment} as a fun activity to do. Does this work for you? ')
  else:
    print(f'You have selected {entertainment} as a fun activity for you to do while on your trip. ')

new_entertainment(confirm_choice)