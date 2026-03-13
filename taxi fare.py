def calculate_fare(distance):
    base_fare = 50
    distance_rate = 10

    return base_fare + (distance * distance_rate)


trips = [5, 10, 3]

total_fare = 0

for i, distance in enumerate(trips):
    fare = calculate_fare(distance)
    print(f"Trip {i+1}: ${fare}")
    total_fare += fare

print("Total Fare:", "$"+str(total_fare))
