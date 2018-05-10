# VoiceTyping

# ABSTRACT:
In this project, we are showing voice typing on 16X2 LCD using Raspberry pi. This is accomplished through the RFCOMM, which is one among various Bluetooth protocols. Various essential libraries like Adafruit and Bluetooth are initially installed on the pi. A simple python program is written to access the GPIO pins of pi to interface the LCD. An android phone with Bluetooth is paired with pi and connection is established through BlueTerm app. While, the connection establishes the program is run which accepts the request and GPIO interfacing is done. Once the connection is established, whatever is said on the voice typing keyboard is displayed on the 16 x 2 LCD. This prototype can be used at various places where speech needs to converted into text and displayed instantly. E.g.: While Airhostess’ are demonstrating the passengers etc. Such requirements can be easily met by this set up.

# Requirements:
•	Raspberry pi 2011.12 (used ,any model shall work)
•	Bluetooth Dongle
•	Android Phone
•	16x32 LCD 
•	Breadboard 
•	Ethernet
•	Jumpers

Prerequisites
•	Download and install the Adafruit Library
•	Install few Bluetooth packages
(Eg: Bluetooth blueman bluez)
•	Install Bluetooth libraries
•	Install GPIO support libraries
Raspberry Pi pin setup
Connections to the LCD display is made using the packages of Adafruit, however the GPIOs used should be set to the proper pins of the LCD display as given below:
Code:

# Raspberry pi pin setup
lcd_rs = 18
lcd_en = 23
lcd_d4 = 24
lcd_d5 = 16
lcd_d6 = 20
lcd_d7 = 21
lcd_backlight = 2

Pairing with raspberry pi over Bluetooth

Open the bluetoothctl utility by below command in the terminal :

sudo bluetoothctl

Enter below commands in given order:

[bluetooth]# power on
[bluetooth]# agent on
[bluetooth]# discoverable on
[bluetooth]# pairable on
[bluetooth]# scan on

Once your device is detected pair it as follows

[bluetooth] pair  <bluetooth address>

# IN THE APP:
Open the BlueTerm App on your Android phone
Connect to the paired Raspberry pi on the Bluetooth terminal
At the same time run the program on the pi.
Now select the Google Voice Typing Keyboard and start speaking, it will appear on the LCD. 



