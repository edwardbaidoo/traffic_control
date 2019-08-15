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