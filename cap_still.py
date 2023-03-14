#!/usr/bin/python3

from picamera2 import Picamera2
from time import sleep

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1440, 1080)})
picam2.configure(camera_config)
picam2.set_controls({"ExposureTime": 35000, "AnalogueGain": 6.0})
picam2.start()
picam2.capture_file("/var/www/html/test.jpg")
picam2.stop()
