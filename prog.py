import bluetooth
import RPi.GPIO as GPIO   #calling for header file which helps in using GPIOs of PI
import Adafruit_CharLCD as LCD
# Raspberry Pi pin setup
lcd_rs = 18
lcd_en = 23
lcd_d4 = 24
lcd_d5 = 16
lcd_d6 = 20
lcd_d7 = 21
lcd_backlight = 2
# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
 
server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
 
port = 1
server_socket.bind(("",port))
server_socket.listen(1)
 
client_socket,address = server_socket.accept()
print "Accepted connection from ",address
while 1:
 
 data = client_socket.recv(1024)
 print "Received: %s" % data
 if (data != ""):
  lcd.clear()
  print (len(data))
  if (len(data) > 16):  #breaking long strings into 2 parts
   i = len(data)-16
   a,b = data[:16], data[16:]  #first string will be of 16 char
   lcd.message(a)
   lcd.message('\n')
   lcd.message(b)
   print i
   print a
   print b
  else:
   lcd.message(data)
  
 if (data == "clear"):
  lcd.clear()
  
 if (data == "q"):
  print ("Quit")
  break
 
client_socket.close()
server_socket.close()