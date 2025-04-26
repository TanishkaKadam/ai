# Rule-based expert system for airline scheduling and cargo assignment

def get_flight_info():
    print("📦 Enter Cargo Details:")
    destination = input("Destination (e.g., New York, London, Dubai): ").strip().lower()
    weight = float(input("Cargo weight (kg): "))
    cargo_type = input("Cargo type (general/perishable/hazardous): ").strip().lower()
    return destination, weight, cargo_type

def match_flight(destination, weight, cargo_type):
    # Sample flight data
    flights = [
        {"flight": "AI101", "to": "new york", "capacity": 1000, "types": ["general", "perishable"]},
        {"flight": "AI202", "to": "london", "capacity": 1500, "types": ["general", "hazardous"]},
        {"flight": "AI303", "to": "dubai", "capacity": 1200, "types": ["general", "perishable", "hazardous"]},
        {"flight": "AI404", "to": "london", "capacity": 800,  "types": ["general"]},
    ]

    matched = []
    for flight in flights:
        if flight["to"] == destination and weight <= flight["capacity"] and cargo_type in flight["types"]:
            matched.append(flight)

    return matched

def expert_system():
    print("✈️ Airline Scheduling & Cargo Expert System")
    
    destination, weight, cargo_type = get_flight_info()
    matches = match_flight(destination, weight, cargo_type)

    if matches:
        print("\n📋 Available Flight(s) for your Cargo:")
        for f in matches:
            print(f"- Flight {f['flight']} to {f['to'].title()} | Capacity: {f['capacity']} kg | Allowed: {', '.join(f['types'])}")
    else:
        print("\n⚠️ No available flights match your cargo requirements.")
        print("Consider splitting cargo or contacting operations manually.")

# ===== MAIN =====
if __name__ == '__main__':
    expert_system()
