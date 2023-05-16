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
 
    # Returns the channel for this TV
    def get_channel(self):
        return self.channel
    
    # Sets a new channel for this TV
    def set_channel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
            
    # Gets the volume level for this TV
    def get_volume(self):
        return self.volume_level

    # Sets a new volume level for this TV
    def set_volume(self, volume_level):
        if self.on and 1 <= volume_level <= 7:
            self.volume_level = volume_level
            
    # Increases the channel number by 1
    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1

    # Decreases the channel number by 1
    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1
    
    # Increases the volume level by 1
    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1

    # Decreases the volume level by 1
    def volume_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1
            
# a Test Driver program named TestTV that will create two objects from Class TV and will produce the following output:
    # tv1's channel is 30 and volume level is 3 
    # tv2's channel is 3 and volume level is 2 channel
    
class TestTV:
    def __init__(self):
        self.tv1 = TV()
        self.tv2 = TV()

    def run(self):
        self.tv1.turn_on()
        self.tv1.set_channel(30)
        self.tv1.set_volume(3)

        self.tv2.turn_on()
        self.tv2.set_channel(3)
        self.tv2.set_volume(2)

        print('\033[1;95;40m'f"TV 1 Channel:", self.tv1.get_channel())
        print('\033[1;95;40m'f"TV 1 Volume:", self.tv1.get_volume())

        print('\033[1;34;40m'f"TV 2 Channel:", self.tv2.get_channel())
        print('\033[1;34;40m'f"TV 2 Volume:", self.tv2.get_volume())


# Test the TV class
test = TestTV()
test.run()
    