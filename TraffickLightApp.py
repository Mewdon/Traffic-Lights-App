from TrafficLight import TrafficLightInformation
from Task1 import count_occurrences
from Task2 import total_active_time
from Task3 import green_active_times
from Task5 import count_mistakes


def parse_file_to_objects():
    traffic_light_array = []
    filename = 'data.txt'

    with open(filename, 'r') as file:
        next(file)

        for line in file:
            parts = line.strip().split(',')
            new_traffic_light = TrafficLightInformation(parts[0], parts[1], parts[2], parts[3], parts[4])
            print(new_traffic_light)
            traffic_light_array.append(new_traffic_light)

    return traffic_light_array


traffic_lights = parse_file_to_objects()

# Task 1
count_occurrences(traffic_lights)
# Task 2
total_active_time(traffic_lights)
# Task 3
green_active_times(traffic_lights)
# Task 5
count_mistakes(traffic_lights)
