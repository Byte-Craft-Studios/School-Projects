from turtle import*

def Baum(n):
    if n>3:
        fd(n)
        right(45)
        Baum(n/2)
        left(90)
        Baum(n/2)
        right(45)
        fd(-n)

#Positionieren der Turtle
pu()
right(90)
fd(200)
left(180)
pd()

def Quadratbaum(n):
    
    if n>10:
        left(90)
        fd(n/2)
        right(90)
        fd(n)
        left(45)
        Quadratbaum(n/2)
 
        right(135)
        fd(n)
        left(45)
         
        Quadratbaum(n/2)
        right(135)
        fd(n)
        right(90)
        fd(n/2)
        right(90)
        
speed(10**2)
#Baum(90)
Quadratbaum(100)
done()
