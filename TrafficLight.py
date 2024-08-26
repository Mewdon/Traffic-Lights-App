class TrafficLightInformation:
    def __init__(self, red, yellow, green, time_active, time):
        self.red = int(red)
        self.yellow = int(yellow)
        self.green = int(green)
        self.time_active = int(time_active)
        self.time = time

    def __repr__(self):
        return f"TrafficLightInformation(Red={self.red}, Yellow={self.yellow}, Green={self.green}, TimeActive={self.time_active}, Time={self.time})"
