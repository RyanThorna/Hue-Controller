__author__ = 'Dave'
#!/usr/bin/python
try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
from phue import Bridge

import time

toggle1 = 0
toggle2 = 0
toggle3 = 0
toggle4 = 0
hue = 0
store_list = []

b=Bridge("192.168.1.159")
##b.connect()

master = Tk(className="Hue Controller")
master.geometry("300x400+810+340")

lights = b.get_light_objects('id')

def lampselect1():
    global toggle1
    global b1
    global b
    if toggle1 == 0:
        b1.config(text="selected")
        b.set_light(1, 'on', True)
        toggle1 = 1
    elif toggle1 == 1:
        b1.config(text="lamp 1")
        toggle1 = 0
def lamp1_toggle():
    if b1_toggle.cget("text") == "off":
        b.set_light(1,'on',True)
        b1_toggle.config(text="on")
    else:
        b.set_light(1,'on',False)
        b1_toggle.config(text="off")
def lampselect2():
    global toggle2
    global b2
    global b
    if toggle2 == 0:
        b2.config(text="selected")
        b.set_light(2, 'on', True)
        toggle2 = 2
    elif toggle2 == 2:
        b2.config(text="lamp 2")
        toggle2 = 0
def lamp2_toggle():
    if b2_toggle.cget("text") == "off":
        b.set_light(2,'on',True)
        b2_toggle.config(text="on")
    else:
        b.set_light(2,'on',False)
        b2_toggle.config(text="off")
def lampselect3():
    global toggle3
    global b3
    global b
    if toggle3 == 0:
        b3.config(text="selected")
        b.set_light(3, 'on', True)
        toggle3 = 3
    elif toggle3 == 3:
        b3.config(text="lamp 3")
        toggle3 = 0
def lamp3_toggle():
    if b3_toggle.cget("text") == "off":
        b.set_light(3,'on',True)
        b3_toggle.config(text="on")
    else:
        b.set_light(3,'on',False)
        b3_toggle.config(text="off")
def hueslider(val):
    global slider1
    global toggle1
    global toggle2
    global toggle3
    global b
    lamparray = [toggle1, toggle2, toggle3]
    while 0 in lamparray:
        lamparray.remove(0)
    b.set_light(lamparray, 'hue', int(val))
def satslider(val):
    global slider2
    global toggle1
    global toggle2
    global toggle3
    global b
    lamparray = [toggle1, toggle2, toggle3]
    while 0 in lamparray:
        lamparray.remove(0)
    b.set_light(lamparray, 'sat', int(val))
def brightslider(val):
    global slider3
    global toggle1
    global toggle2
    global toggle3
    global b
    lamparray = [toggle1, toggle2, toggle3]
    while 0 in lamparray:
        lamparray.remove(0)
    b.set_light(lamparray, 'bri', int(val))
def scrollfunction():
    global store_list
    if (b4.cget("text")=="start scroll"):
        b4.config(text="stop scroll")
        i = 0
        while (b4.cget("text")=="stop scroll"):
            hue = store_list[3*i]
            sat = store_list[3*i+1]
            bri = store_list[3*i+2]
            timedelay = int(transition.get())
            command = {'transitiontime' : int(10*timedelay), 'on' : True, 'hue' : hue, 'sat' : sat, 'bri' : bri}
            b.set_light([1,2,3],command)
            time.sleep(timedelay)
            i += 1
            if (i == (len(store_list)/3)):
                i = 0
            master.update()


    else:
        b4.config(text="start scroll")


def setcolor():
    global store_list
    button_name = custom_wash.cget("text")
    button_number = int(button_name[10:]) + 1
    button_name = button_name[:10] + str(button_number)
    custom_wash.config(text=button_name)
    stored_hue = slider1.get()
    stored_sat = slider2.get()
    stored_bright = slider3.get()
    store_list.append(stored_hue)
    store_list.append(stored_sat)
    store_list.append(stored_bright)
def clearcolors():
    global store_list
    custom_wash.config(text="set color 1")
    store_list = []

b1 = Button(master, text="lamp 1", command=lampselect1)
b1.config(height=1, width=10)
b1.place(x=5, y=25)

b1_toggle = Button(master, text="on", command=lamp1_toggle)
b1_toggle.config(height=1, width=10)
b1_toggle.place(x=5, y=60)

b2 = Button(master, text="lamp 2", command=lampselect2)
b2.config(height=1, width=10)
b2.place(x=105, y=25)

b2_toggle = Button(master, text="on", command=lamp2_toggle)
b2_toggle.config(height=1, width=10)
b2_toggle.place(x=105, y=60)

b3 = Button(master, text="lamp 3", command=lampselect3)
b3.config(height=1, width=10)
b3.place(x=205, y=25)

b3_toggle = Button(master, text="on", command=lamp3_toggle)
b3_toggle.config(height=1, width=10)
b3_toggle.place(x=205, y=60)

slider1 = Scale(master,from_=0, to=65534, orient=HORIZONTAL)
slider1.config(length=217, command=hueslider)
slider1.place(x=75, y=100)

slider2 = Scale(master,from_=0, to=254, orient=HORIZONTAL)
slider2.config(length=217, command=satslider)
slider2.place(x=75, y=150)

slider3 = Scale(master,from_=0, to=254, orient=HORIZONTAL)
slider3.config(length=217, command=brightslider)
slider3.place(x=75, y=200)

label1 = Label(master, text="hue: ")
label1.place(x=5, y=119)

label2 = Label(master, text="sat: ")
label2.place(x=5, y=169)

label3 = Label(master, text="bright: ")
label3.place(x=5, y=219)

b4 = Button(master, text="start scroll", command=scrollfunction)
b4.config(height=1, width=10)
b4.place(x=105, y=255)

custom_wash = Button(master, text="set color 1", command=setcolor)
custom_wash.config(height=1, width=10)
custom_wash.place(x=205, y=320)

delete_wash = Button(master, text="clear colors", command=clearcolors)
delete_wash.config(height=1, width=10)
delete_wash.place(x=205, y=350)

transition = Entry(master, width=2)
transition.place(x=210, y=295)


label4 = Label(master, text="transition time: ")
label4.place(x=120, y=295)

label5 = Label(master, text="sec")
label5.place(x=235, y=295)

mainloop()