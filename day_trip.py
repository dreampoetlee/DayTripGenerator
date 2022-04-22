import random

# Trip Greeting Message
greeting_message = 'Thank you for using our Day Trip Generator to plan your upcoming day excursion.'
print(greeting_message)

# Destination Code Block
# Created destination list and randomily selected destination
trip_destinations = ['Provincetown, MA', 'Fort Lauderdale, FL', 'San Juan, PR', 'Fire Island, NY', 'Palm Springs, CA', 'Honolul, HI']
selected_destination = random.randrange(len(trip_destinations))

# Created destination list and randomily selected restaurants 
best_restaurants = ['Crown & Anchor Restaurant', 'Heritage', 'Oasis Tapas & Lounge', 'The Blue Whale', 'Hunters Palm Springs', 'Bacchus Waikiki']
selected_restaurant = random.randrange(len(best_restaurants))

# Created destination list and randomily selected mode of transportation
best_transportations = ['Walk', 'Electric Bike', 'Bus', 'Train', 'Yacht', 'Helicopter']
selected_transportation = random.randrange(len(best_transportations))

# Created destination list and randomily selected entertainment 
best_entertainments = ['Walking Tours', 'Segway Tours', 'Bus Tours', 'Cooking Classes', 'Amusement Parks', 'Theater']
selected_entertainment = random.randrange(len(best_entertainments))

print(f'For your Summer Day Trip excursion we have selected {trip_destinations[selected_destination]} for your destination, {best_restaurants[selected_restaurant]} for your perfect meal, {best_transportations[selected_transportation]} as the best way to travel around town, and {best_entertainments[selected_entertainment]} as a fun day activity. Are you excited about the selections that we made? ')

# Function for user input
confirm_choice = input('Please enter y/n to confirm these travel options. ')

def user_choice(confirm_options):
  while confirm_options != 'y':
    selected_options = random.randrange([(len(trip_destinations)), (len(best_restaurants)), (len(best_transportations)), (len(best_entertainments))])
    confirm_options = input(f'We are sorry that those options did not work for you. We have selected {selected_options} as another set of options for you. Does these options work for you? ')
  else:
    print(f'You have selected {trip_destinations[selected_destination]} as the destination for your trip. You will be dining at the {best_restaurants[selected_restaurant]} during the course of the day. You will travel around town via {best_transportations[selected_transportation]}, and for fun you will do {best_entertainments[selected_entertainment]}. We hope that you enjoy the trip that we have planned for you.')

user_choice(confirm_choice)


















# # Need four different lists

# # List 1: Destination

# random_destination = random.randrange(len(trip_destinations))

# print(trip_destinations[random_destination])

# print('')

# # List 2: Restaurants


# print(best_restaurants[random_restaurants])

# print(' ')



# print(best_way_to_get_around[random_transportation])

# print('')



# print(things_to_do[random_entertainment])

# print('')