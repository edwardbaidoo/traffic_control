from gpiozero import LED
import time

#### NOTES on GPIO PINS
# Number of Traffic Heads = 2
# Number of Leds per head = 3
# Pins per head = 4(3 GPIO, 1 Ground)
# Ground = Pin6/39

#### HEAD 1 details
# LED1 = h1l1 = 15(22)
# LED2 = h1l2 = 16(23)
# LED3 = h1l3 = 18(24)

#### HEAD 2 Details
# LED 1 = h2l1 = 38(20)
# LED 2 = h2l2 = 40(21)
# LED 3 = h2l3 = 37(26)

#Initialize LEDs

h1l1 = LED(22)
h1l2 = LED(23)
h1l3 = LED(24)

h2l1 = LED(20)
h2l2 = LED(21)
h2l3 = LED(26)

h1l1.on()
time.sleep(2)
h1l1.off()
h1l2.blink(2,0.5)
time.sleep(10)
h1l2.off()
h1l3.on()
time.sleep(2)
h1l3.off()

h2l1.on()
time.sleep(2)
h2l1.off()
h2l2.blink(2,0.5)
time.sleep(10)
h2l2.off()
h2l3.on()
time.sleep(2)
h2l3.off()