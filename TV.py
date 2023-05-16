# The TV class defines TV Sets
class TV:
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False

# The current channel (1 to 120) of this TV
# The current volume level (1 to 7) of this TV
# Indicates whether this TV is on/off

    # Turn on this TV
    def turn_on(self):
        self.on = True
        
    # Turn off this TV
    def turn_off(self):
        self.on = False