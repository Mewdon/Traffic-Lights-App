# Find number of lines with mistakes (multiple colours active at the same time or no colours active)
def count_mistakes(traffic_lights):
    mistakes_count = 0

    for light in traffic_lights:
        colors_active = sum([light.red, light.yellow, light.green])

        if colors_active == 0 or colors_active > 1:
            mistakes_count += 1

    print(f"Number of lines with mistakes (multiple colors active or no colors active): {mistakes_count}")
