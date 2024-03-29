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


# Test LED
# h1l1.on()
# time.sleep(2)
# h1l1.off()
# h1l2.blink(2,0.5)
# time.sleep(10)
# h1l2.off()
# h1l3.on()
# time.sleep(2)
# h1l3.off()

# h2l1.on()
# time.sleep(2)
# h2l1.off()
# h2l2.blink(2,0.5)
# time.sleep(10)
# h2l2.off()
# h2l3.on()
# time.sleep(2)
# h2l3.off()

#Response actions
##Case 1
def case1():
    h1l3.on()
    h2l1.on()
    time.sleep(10)
    h1l3.off()
    h2l1.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()
    h1l1.on()
    h2l3.on()
    time.sleep(10)
    h1l1.off()
    h2l3.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()

##Case 2
def case2():
    h1l3.on()
    h2l1.on()
    time.sleep(8)
    h1l3.off()
    h2l1.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()
    h1l1.on()
    h2l3.on()
    time.sleep(12)
    h1l1.off()
    h2l3.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()

##Case 3
def case3():
    h1l3.on()
    h2l1.on()
    time.sleep(5)
    h1l3.off()
    h2l1.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()
    h1l1.on()
    h2l3.on()
    time.sleep(15)
    h1l1.off()
    h2l3.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()

##Case 4
def case4():
    h1l3.on()
    h2l1.on()
    time.sleep(12)
    h1l3.off()
    h2l1.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()
    h1l1.on()
    h2l3.on()
    time.sleep(8)
    h1l1.off()
    h2l3.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()

##Case 5
def case5():
    h1l3.on()
    h2l1.on()
    time.sleep(15)
    h1l3.off()
    h2l1.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()
    h1l1.on()
    h2l3.on()
    time.sleep(5)
    h1l1.off()
    h2l3.off()
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(2)
    h1l2.off()
    h2l2.off()

##Case 6
def case6():
    h1l2.blink(0.5,0.5)
    h2l2.blink(0.5,0.5)
    time.sleep(100)

#conditions
if finY >= -0.2 and finY <= 0.2:
    print("Traffic load normal, no changes to be made")
    case1()
elif finY < -0.2 and finY >= -0.5:
    print("Traffic Minimal, saving time")
    case2()
elif finY < -0.5 and finY >= -1.0:
    print("Traffic Very low, Routing time")
    case3()
elif finY > 0.2 and finY <= 0.5:
    print("Increased traffic load, Increasing GLT")
    case4()
elif finY > 0.5 and finY <= 1.0:
    print("Extreme traffic condition, Increasing GLT to P1")
    case5()
else:
    print("Undetermined Traffic behvior, Human Intervention necessary")
    case6()

# if y2 >= -0.2 and y2 <= 0.2:
#     print("Traffic load normal, no changes to be made")
#     case1()
# elif y2 < -0.2 and y2 >= -0.5:
#     print("Traffic Minimal, saving time")
#     case4()
# elif y2 < -0.5 and y2 >= -1.0:
#     print("Traffic Very low, Routing time")
#     case5()
# elif y2 > 0.2 and y2 <= 0.5:
#     print("Increased traffic load, Increasing GLT")
#     case2()
# elif y2 > 0.5 and y2 <= 1.0:
#     print("Extreme traffic condition, Increasing GLT to P1")
#     case3()
# else:
#     print("Undetermined Traffic behvior, Human Intervention necessary")
#     case6()