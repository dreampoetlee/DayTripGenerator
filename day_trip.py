import random

# Trip Greeting Message
greeting_message = 'Thank you for using our Day Trip Generator to plan your upcoming day excursion.'
print(greeting_message)

# Destination Code Block
# Created destination list and randomily selected destination
trip_destinations = ['Provincetown, MA', 'Fort Lauderdale, FL', 'San Juan, PR', 'Fire Island, NY', 'Palm Springs, CA', 'Honolul, HI']
selected_destination = random.randrange(len(trip_destinations))
print(f'We have selected {trip_destinations[selected_destination]} for your destination! Are you excited about going to this location?')

# Function for user input
confirm_choice = input('Please enter y/n to confirm this destination. ')

def user_choice(confirm_choice) :
  while confirm_choice != 'y' :
    print(f'We are sorry that option did not work for you. We have selected {trip_destinations[selected_destination]} as another option. Does this work for you?')

  # else:
  #   confirm_choice == 'y' :



user_choice(confirm_choice)


















# # Need four different lists

# # List 1: Destination

# random_destination = random.randrange(len(trip_destinations))

# print(trip_destinations[random_destination])

# print('')

# # List 2: Restaurants
# best_restaurants = ['Crown & Anchor Restaurant', 'Heritage', 'Oasis Tapas & Lounge', 'The Blue Whale', 'Hunters Palm Springs', 'Bacchus Waikiki']
# random_restaurants = random.randrange(len(best_restaurants))

# print(best_restaurants[random_restaurants])

# print(' ')

# # List 3: Mode of Transportation
# best_way_to_get_around = ['Walk', 'Electric Bike', 'Bus', 'Train', 'Yacht', 'Helicopter']
# random_transportation = random.randrange(len(best_way_to_get_around))

# print(best_way_to_get_around[random_transportation])

# print('')

# # List 4: Entertainment
# things_to_do = ['Walking Tours', 'Segway Tours', 'Bus Tours', 'Cooking Classes', 'Amusement Parks', 'Theater']
# random_entertainment = random.randrange(len(things_to_do))

# print(things_to_do[random_entertainment])

# print('')