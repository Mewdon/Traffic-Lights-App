# Find all times when Green was active (by time)
def green_active_times(traffic_lights):
    green_times = [light.time for light in traffic_lights if light.green > 0]

    print("Times when Green was active:")
    for time in green_times:
        print(time)
