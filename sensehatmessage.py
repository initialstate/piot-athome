from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

try:
  sense.show_message("Write anything you want!")
except KeyboardInterrupt:
  sense.clear()
  exit()
