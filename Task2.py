# Find how long each colour was active for.
def total_active_time(traffic_lights):
    red_time = 0
    yellow_time = 0
    green_time = 0

    for light in traffic_lights:
        if light.red:
            red_time += light.time_active
        if light.yellow:
            yellow_time += light.time_active
        if light.green:
            green_time += light.time_active

    print(f"Total Red Active Time: {red_time} seconds")
    print(f"Total Yellow Active Time: {yellow_time} seconds")
    print(f"Total Green Active Time: {green_time} seconds")
