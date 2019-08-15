################
##    MATH    ##
################
#Guideline for vatiables
#design capacity - d
#Minimum input(data read) - x
#maximum input(data read) - x
#represent as percent value - v
#minimum norm range - a
#maximum norm range - b
#norm value - y - (-1 >= y <= 1)

# Formula used 
#   v=(x-d)/d*100
#   y=(v-a)/(b-a)


#initialization
d1 = int(input("Enter Lane1 design Capacity:"))
x1 = int(input("Enter Lane1 Current vehicle count:"))
v1=0
a1 = 0
b1=100
y1 = 0

#percentage
def calcPercent(d1,x1,v1):
    """Calculate in percentage an increment or decrement in number of Cars"""
    v1 = (x1-d1)/d1*100
    return v1


# print(calcPercent(d,x,v))
v1 = calcPercent(d1,x1,v1)

#normalization
def norm(v1,a1,b1,y1):
    """Normalize percentage value to a range of -1.0 to 1.0"""
    y1=(v1-a1)/(b1-a1)
    return y1

print(norm(v1,a1,b1,y1))
y1 = norm(v1,a1,b1,y1)


#lane2
#initialization
d2 = int(input("Enter Lane2 design Capacity:"))
x2 = int(input("Enter Lane2 Current vehicle count:"))
v2=0
a2 = 0
b2=100
y2 = 0

#percentage
def calcPercent(d2,x2,v2):
    """Calculate in percentage an increment or decrement in number of Cars"""
    v2 = (x2-d2)/d2*100
    return v2


# print(calcPercent(d,x,v))
v2 = calcPercent(d2,x2,v2)

#normalization
def norm(v2,a2,b2,y2):
    """Normalize percentage value to a range of -1.0 to 1.0"""
    y2=(v2-a2)/(b2-a2)
    return y2

print(norm(v2,a2,b2,y2))
y2 = norm(v2,a2,b2,y2)

if y1 > y2:
    print("Lane1 has most activity\n")
    finY = y1
    print("Lane1 norm ={}".format(finY))
elif y2 > y1:
    print("Lane2 has most activity\n")
    finY = y2
    print("Lane2 norm ={}".format(finY))

################
##   LIGHTS   ##
################

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
    case1()
    case1()
elif finY < -0.2 and finY >= -0.5:
    print("Traffic Minimal, saving time")
    case2()
    case2()
    case2()
elif finY < -0.5 and finY >= -1.0:
    print("Traffic Very low, Routing time")
    case3()
    case3()
    case3()
elif finY > 0.2 and finY <= 0.5:
    print("Increased traffic load, Increasing GLT")
    case4()
    case4()
    case4()
elif finY > 0.5 and finY <= 1.0:
    print("Extreme traffic condition, Increasing GLT to P1")
    case5()
    case5()
    case5()
else:
    print("Undetermined Traffic behvior, Human Intervention necessary")
    case6()
    case6()
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