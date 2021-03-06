#!/usr/bin/env python

import lcddriver
import time
import sys
import subprocess

# ------------------------------------------------------------------------------------
# Check to see if LCD is connected if not then stop here
# ------------------------------------------------------------------------------------
lcd_i2c = ['27', '3f']
current_lcd_i2c = ''

for i2c_address in lcd_i2c:
  lcd_status = subprocess.check_output(["/home/pi/emonpi/lcd/emonPiLCD_detect.sh", "%s" % i2c_address])
  if lcd_status.rstrip() == 'True':
    print "I2C LCD DETECTED Ox%s" % i2c_address
    current_lcd_i2c = "0x%s" % i2c_address
    break

if lcd_status.rstrip() == 'False':
  print ("I2C LCD NOT DETECTED on either 0x" + str(lcd_i2c) + " ...exiting LCD script")
  sys.exit(1)
  
lcd = lcddriver.lcd(int(current_lcd_i2c, 16))

# ------------------------------------------------------------------------------------
# Display update in progress update
# ------------------------------------------------------------------------------------
lcd.backlight = 1
lcd.lcd_display_string("Updating........", 1)
lcd.lcd_display_string("DO NOT UNPLUG!  ",2)
time.sleep(1)
sys.exit()
