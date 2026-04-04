from data import DATA

def plan_trip(query):
    query = query.lower()

    destination = None
    for city in DATA:
        if city in query:
            destination = city
            break

    if not destination:
        return {"error": "Destination not found"}

    days = 3

    prefs = []
    if "beach" in query:
        prefs.append("beaches")
    if "night" in query:
        prefs.append("nightlife")
    if "food" in query:
        prefs.append("food")
    if "nature" in query:
        prefs.append("nature")
    if "culture" in query:
        prefs.append("culture")

    if not prefs:
        prefs = ["beaches", "food"]

    places = []
    for p in prefs:
        places += DATA[destination][p]

    itinerary = {}
    for i in range(days):
        itinerary[f"Day {i+1}"] = places[i::days]

    return {
        "destination": destination.title(),
        "days": days,
        "preferences": ", ".join(prefs),
        "itinerary": itinerary
    }
