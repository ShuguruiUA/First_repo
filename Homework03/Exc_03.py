base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):
    global price_per_km
    global base_rate
    total = distance_km * price_per_km + base_rate
    global total_trip 
    total_trip += 1
    print(total)
    return total
calculate_trip_price(12)
calculate_trip_price(12)
calculate_trip_price(12)
calculate_trip_price(12)
print(total_trip)
