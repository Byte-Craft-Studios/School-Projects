from tkinter import *
from math import *
#Funktionsgleichung
def f(x):
    return a*x*x+b*x+c

def buttonPlusClick():
    a= float(entryZahla.get())
    b= float(entryZahlb.get())
    c= float(entryZahlc.get())
    if a!= 0:
        p=b/a
        q=c/a
        d= p*p/4-q
        if d<0:
            x1='keine'
            x2='Lösung'
        elif d==0:
            x1=-p/2
            x2='-'
            x1=round(x1,3)
        elif d>0:
            x1= -p/2+sqrt(d)
            x2= -p/2-sqrt(d)
            x1=round(x1,3)
            x2=round(x2,3)
        else:
            x1='try'
            x2='again'
    elif a==0 and b==0:
        if c==0:
            x1='unendlich'
            x2='unendlich'
        else:
            x1='keine'
            x2='Lösung'
    elif a==0:
        x1=-c/b
        x2='-'
        x1=round(x1,3)
    else:
        x1='try'
        x2='again'
        
    x1= str(x1)
    x2= str(x2)
    labelErgebnis2.config(text='{}'.format(x1))
    labelErgebnis4.config(text="{}".format(x2))
    
def kszeichnen():
    global can
    yb=0
    xb=0
    x=(xb-xm)/xe
    y=(ym-yb)/ye  
    xb=int(xm+x*xe)
    yb=int(ym-y*ye)     
    can.create_line(0,ym,w,ym)
    can.create_line(xm,0,xm,h) 
    anzahl=(w+xm)//xe
    for i in range(1, anzahl):
        xkl=xm-20*i
        can.create_line(xkl, ym-2, xkl, ym+2)

    for i in range (1,anzahl):
        xkr=xm+20*i
        can.create_line(xkr, ym-2, xkr, ym+2) 
    
    anzahl=(h+ym)//ye    
    for i in range(1,anzahl):
        yko=ym+20*i
        can.create_line(xm-2, yko, xm+2, yko)
    for i in range(1,anzahl):
        yku=ym-20*i
        can.create_line(xm-2, yku, xm+2, yku)     

        
def funktionzeichnen():
    xa=0
    ya=0   
    for xb in range(0,w):       
        x=(xb-xm)/xe
        y=f(x)
        yb=int(ym-y*ye)
        if yb>0 and yb<h:
            can.create_line(xa, ya, xb, yb)   
        xa=xb
        ya=yb
                
def resize(event):
    global w, h
    w = can.winfo_width()
    h = can.winfo_height()
    kszeichnen()
    funktionzeichnen()

def bpressed(event):
    global xmaus, ymaus
    xmaus = event.x
    ymaus = event.y

def drag(event):
    global xm, ym, xmaus, ymaus
    # xm = xm+event.x-xmaus
    # ym = ym+event.y-ymaus
    
    xm = event.x
    ym = event.y
    
    can.delete('all')
    kszeichnen()
    funktionzeichnen()
    
def breleased(event):
    global xm, ym, xmaus, ymaus
    xm = xm+event.x-xmaus
    ym = ym+event.y-ymaus
    can.delete('all')
    kszeichnen()
    funktionzeichnen()
        
def buttonDarstellungclick():
    global a,b,c
    global x, y, ym, xm
    global can
    a= float(entryZahla.get())
    b= float(entryZahlb.get())
    c= float(entryZahlc.get())
    FensterDarstellung= Toplevel()
    FensterDarstellung.title('Darstellung')
    FensterDarstellung.geometry('400x400+800+200')
    darstellungparabel=Canvas(master=Fenster, bg='grey')
    can = Canvas(master=FensterDarstellung, bg='lightgray')
    can.pack(side='left', fill='both', expand='True')
    #Koordinatensystem
    can.bind('<Configure>',resize)
    can.bind('<Button-1>', bpressed)
    can.bind('<B1-Motion>', drag)
    # can.bind('<ButtonRelease-1>', breleased)
    
    kszeichnen()
    funktionzeichnen()

  
Fenster = Tk()
Fenster.title('kleiner Rechner')
Fenster.geometry('600x600')
#ye und xe sind Pixel pro Einheit, bilden Koordinatenursprung
w=400; h=400; xm=w//2; ym=h//2; xe=20; ye=20; can=Canvas()
xmaus = 0; ymaus = 0

labelZahla = Label(master=Fenster, bg='#FFDFC9', text='Zahl a')
labelZahla.place(x=54, y=24, width=100, height=54)

entryZahla= Entry(master=Fenster, bg='white')
entryZahla.insert(0,'1')
entryZahla.place(x=164, y=24, width=100, height=54)

labelZahlb = Label(master=Fenster, bg='#FFDFC9', text='Zahl b')
labelZahlb.place(x=54, y=100, width=100, height=54)

entryZahlb= Entry(master=Fenster, bg='white')
entryZahlb.insert(0,'0')
entryZahlb.place(x=164, y=100, width=100, height=54)

labelZahlc = Label(master=Fenster, bg='#FFDFC9', text='Zahl c')
labelZahlc.place(x=54, y=176, width=100, height=54)

entryZahlc= Entry(master=Fenster, bg='white')
entryZahlc.insert(0,'0')
entryZahlc.place(x=164, y=176, width=100, height=54)

buttonPlus = Button(master=Fenster, text='Löse ax*2+bx+c=0', bg='#D5E88F', command=buttonPlusClick)
buttonPlus.place(x=99, y=252, width=120, height=54)


buttonDarstellung = Button(master=Fenster, text='Darstellung', bg='#D5E88F', command=buttonDarstellungclick)
buttonDarstellung.place(x=264, y=252, width=120, height=54)


labelErgebnis=Label(master=Fenster, bg='white', text='x1')
labelErgebnis.place(x=54, y=328, width=100, height=54)

labelErgebnis2=Label(master=Fenster, bg='white', text='')
labelErgebnis2.place(x=164, y=328, width=100, height=54)

labelErgebnis3=Label(master=Fenster, bg='white', text='x2')
labelErgebnis3.place(x=54, y=404, width=100, height=54)

labelErgebnis4=Label(master=Fenster, bg='white', text='')
labelErgebnis4.place(x=164, y=404, width=100, height=54)

Fenster.mainloop()