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

x = int(input("enter number:"))
#initialization
d = 70
v=0
a = 0
b=100
y = 0

#percentage
def calcPercent(d,x,v):
    v = (x-d)/d*100
    return v


print(calcPercent(d,x,v))
v = calcPercent(d,x,v)

#normalization
def norm(v,a,b,y):
    y=(v-a)/(b-a)
    return y

print(norm(v,a,b,y))
