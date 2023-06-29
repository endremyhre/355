""" Testing av adafruit 16channel servo driver.
    basert på eksempelkode fra adafruit: 
    https://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi/overview """

from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

kit.continuous_servo[0].throttle = 0