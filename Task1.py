# Find the number of red, yellow & green occurrences.
def count_occurrences(traffic_lights):
    red_count = 0
    yellow_count = 0
    green_count = 0

    for light in traffic_lights:
        red_count += light.red
        yellow_count += light.yellow
        green_count += light.green

    print(f"Red count: {red_count}")
    print(f"Yellow count: {yellow_count}")
    print(f"Green count: {green_count}")
