
dwarves = ["Doc", "Dopey", "Bashful", "Grumpy"]

planeteer_calls = ["earth", "wind", "fire", "water", "heart"]

cheeses = ["cheddar", "gouda", "camembert"]

def roll_call_dwarves(dwarves):
    for index, dwarf in enumerate(dwarves):
        print(f"{index+1}. {dwarf}")

def summon_captain_planet(planeteer_calls):
    return [call.capitalize() + "!" for call in planeteer_calls]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

# def find_the_cheese(list):
#     for item in list:
#         if item == "cheddar" or item == "gouda" or item == "camembert":
#             return item
#     return None

def find_the_cheese(list):
    for item in list:
        if item in cheeses:
            return item
    return None