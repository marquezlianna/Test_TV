# TV Class
The TV class defines TV sets and provides methods to control their channels and volume levels. It also includes methods to turn the TV on and off.

# Class Attributes
channel: The current channel (1 to 120) of this TV.

volume_level: The current volume level (1 to 7) of this TV.

on: Indicates whether this TV is on or off.


# Class Methods
turn_on(): Turns on the TV.

turn_off(): Turns off the TV.

get_channel(): Returns the current channel of the TV.

set_channel(channel): Sets a new channel for the TV.

get_volume(): Returns the current volume level of the TV.

set_volume(volume_level): Sets a new volume level for the TV.

channel_up(): Increases the channel number by 1.

channel_down(): Decreases the channel number by 1.

volume_up(): Increases the volume level by 1.

volume_down(): Decreases the volume level by 1.


# TestTV Class
The TestTV class serves as a test driver program for the TV class. It creates two TV objects, tv1 and tv2, and sets their channels and volume levels. The program then prints the channel and volume information for both TVs.

# Usage
To test the TV class, create an instance of the TestTV class and call the run() method.

# Test the TV class
test = TestTV()

test.run()

# Output
The TestTV program will produce the following output:

TV 1 Channel: 30

TV 1 Volume: 3

TV 2 Channel: 3

TV 2 Volume: 2

The output displays the channel and volume information for tv1 and tv2 objects as specified in the TestTV class.

# Link
https://drive.google.com/file/d/1gK-5RNS1nBksEGgghJhbIqz0Dkw_vRvt/view?usp=sharing
