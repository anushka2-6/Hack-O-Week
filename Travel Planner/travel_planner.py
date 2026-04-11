from data import destinations
from utils import preprocess

def recommend_place(user_input):
    tokens = preprocess(user_input)

    if "cold" in tokens:
        return ["Manali", "Shimla", "Leh"]
    elif "beach" in tokens:
        return ["Goa", "Maldives", "Andaman"]
    elif "hill" in tokens:
        return ["Darjeeling", "Ooty", "Munnar"]
    elif "religious" in tokens:
        return ["Varanasi", "Tirupati", "Shirdi"]
    elif "city" in tokens:
        return ["Mumbai", "Delhi", "Bangalore"]
    else:
        return ["Goa", "Manali", "Jaipur"]


def show_details(places):
    for place in places:
        if place in destinations:
            print(f"\n📍 {place}")
            print("Best Time:", destinations[place]["best_time"])
            print("Budget:", destinations[place]["budget"])
            print("Famous For:", destinations[place]["famous"])


if __name__ == "__main__":
    print("✈️ AI Travel Planner (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Happy Journey! 😊")
            break

        places = recommend_place(user_input)
        show_details(places)
