__author__ = 'Dave', 'Ryan'
#!/usr/bin/python


#   Import Tkinter for GUI
#-----------------------------------------------------------------------------------------------------------------------
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
#-----------------------------------------------------------------------------------------------------------------------


#   Import library for Hue lights
#-----------------------------------------------------------------------------------------------------------------------
from phue import Bridge
#-----------------------------------------------------------------------------------------------------------------------

from rgb_cie import Converter

converter = Converter()

converter.rgbToCIE1931(255,0,0) #See https://github.com/benknight/hue-python-rgb-converter


#   Import time library for creating delays in scroll function
#-----------------------------------------------------------------------------------------------------------------------
import time
#-----------------------------------------------------------------------------------------------------------------------


#   Toggle variables for each button
#-----------------------------------------------------------------------------------------------------------------------
toggle1 = 0
toggle2 = 0
toggle3 = 0
toggle4 = 0
#-----------------------------------------------------------------------------------------------------------------------


#   List used to store each set of hue/sat/brightness for the scroll function
#-----------------------------------------------------------------------------------------------------------------------
store_list = []
#-----------------------------------------------------------------------------------------------------------------------


#   Connects to the Bridge and creates the main bridge object, b
#-----------------------------------------------------------------------------------------------------------------------
b=Bridge("192.168.1.159")
b.connect()
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the window for the GUI
#-----------------------------------------------------------------------------------------------------------------------
master = Tk(className="Hue Controller")
master.geometry("300x400+810+340")
#-----------------------------------------------------------------------------------------------------------------------


#   Gets all devices connected to the bridge (this program is set up for controlling 1-3 lights)
#-----------------------------------------------------------------------------------------------------------------------
lights = b.get_light_objects('id')
#-----------------------------------------------------------------------------------------------------------------------


#   Function for lamp 1 control button - Toggles whether or not the light will respond to the slider settings
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for lamp 1 power button - Toggles the light on and off
#-----------------------------------------------------------------------------------------------------------------------
def lamp1_toggle():
    if b1_toggle.cget("text") == "off":
        b.set_light(1,'on',True)
        b1_toggle.config(text="on")
    else:
        b.set_light(1,'on',False)
        b1_toggle.config(text="off")
#-----------------------------------------------------------------------------------------------------------------------


#   Function for lamp 2 control button - Toggles whether or not the light will respond to the slider settings
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for lamp 2 power button - Toggles the light on and off
#-----------------------------------------------------------------------------------------------------------------------
def lamp2_toggle():
    if b2_toggle.cget("text") == "off":
        b.set_light(2,'on',True)
        b2_toggle.config(text="on")
    else:
        b.set_light(2,'on',False)
        b2_toggle.config(text="off")
#-----------------------------------------------------------------------------------------------------------------------


#   Function for lamp 3 control button - Toggles whether or not the light will respond to the slider settings
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for lamp 3 power button - Toggles the light on and off
#-----------------------------------------------------------------------------------------------------------------------
def lamp3_toggle():
    if b3_toggle.cget("text") == "off":
        b.set_light(3,'on',True)
        b3_toggle.config(text="on")
    else:
        b.set_light(3,'on',False)
        b3_toggle.config(text="off")
#-----------------------------------------------------------------------------------------------------------------------


#   Function for hue slider - Sets the hue of the selected lights to the value on the slider
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for saturation slider - Sets the sat of the selected lights to the value on the slider
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for brightness slider - Sets the brightness of the selected lights to the value on the slider
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for scroll button - Starts scrolling through the stored hue/sat/bri sets at the specified transition time
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for set color button - Stores the current values of the hue/sat/bri sliders into 'store_list' to be used
#   by the scroll function
#-----------------------------------------------------------------------------------------------------------------------
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
#-----------------------------------------------------------------------------------------------------------------------


#   Function for the clear button - Clears all of the stored colors in 'store_list'
#-----------------------------------------------------------------------------------------------------------------------
def clearcolors():
    global store_list
    custom_wash.config(text="set color 1")
    store_list = []
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the lamp 1 control button
#-----------------------------------------------------------------------------------------------------------------------
b1 = Button(master, text="lamp 1", command=lampselect1)
b1.config(height=1, width=10)
b1.place(x=5, y=25)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the lamp 1 power button
#-----------------------------------------------------------------------------------------------------------------------
b1_toggle = Button(master, text="on", command=lamp1_toggle)
b1_toggle.config(height=1, width=10)
b1_toggle.place(x=5, y=60)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the lamp 2 control button
#-----------------------------------------------------------------------------------------------------------------------
b2 = Button(master, text="lamp 2", command=lampselect2)
b2.config(height=1, width=10)
b2.place(x=105, y=25)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the lamp 2 power button
#-----------------------------------------------------------------------------------------------------------------------
b2_toggle = Button(master, text="on", command=lamp2_toggle)
b2_toggle.config(height=1, width=10)
b2_toggle.place(x=105, y=60)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the lamp 3 control button
#-----------------------------------------------------------------------------------------------------------------------
b3 = Button(master, text="lamp 3", command=lampselect3)
b3.config(height=1, width=10)
b3.place(x=205, y=25)
#-----------------------------------------------------------------------------------------------------------------------

#   Creates the lamp 3 power button
#-----------------------------------------------------------------------------------------------------------------------
b3_toggle = Button(master, text="on", command=lamp3_toggle)
b3_toggle.config(height=1, width=10)
b3_toggle.place(x=205, y=60)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the hue slider
#-----------------------------------------------------------------------------------------------------------------------
slider1 = Scale(master,from_=0, to=65534, orient=HORIZONTAL)
slider1.config(length=217, command=hueslider)
slider1.place(x=75, y=100)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the saturation slider
#-----------------------------------------------------------------------------------------------------------------------
slider2 = Scale(master,from_=0, to=254, orient=HORIZONTAL)
slider2.config(length=217, command=satslider)
slider2.place(x=75, y=150)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the brightness slider
#-----------------------------------------------------------------------------------------------------------------------
slider3 = Scale(master,from_=0, to=254, orient=HORIZONTAL)
slider3.config(length=217, command=brightslider)
slider3.place(x=75, y=200)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the hue slider label
#-----------------------------------------------------------------------------------------------------------------------
label1 = Label(master, text="hue: ")
label1.place(x=5, y=119)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the saturation slider label
#-----------------------------------------------------------------------------------------------------------------------
label2 = Label(master, text="sat: ")
label2.place(x=5, y=169)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the brightness slider label
#-----------------------------------------------------------------------------------------------------------------------
label3 = Label(master, text="bright: ")
label3.place(x=5, y=219)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the scroll button
#-----------------------------------------------------------------------------------------------------------------------
b4 = Button(master, text="start scroll", command=scrollfunction)
b4.config(height=1, width=10)
b4.place(x=105, y=255)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the store color button
#-----------------------------------------------------------------------------------------------------------------------
custom_wash = Button(master, text="set color 1", command=setcolor)
custom_wash.config(height=1, width=10)
custom_wash.place(x=205, y=320)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the clear colors button
#-----------------------------------------------------------------------------------------------------------------------
delete_wash = Button(master, text="clear colors", command=clearcolors)
delete_wash.config(height=1, width=10)
delete_wash.place(x=205, y=350)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the text box for the transition time user input
#-----------------------------------------------------------------------------------------------------------------------
transition = Entry(master, width=2)
transition.place(x=210, y=295)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates the transition time label
#-----------------------------------------------------------------------------------------------------------------------
label4 = Label(master, text="transition time: ")
label4.place(x=120, y=295)
#-----------------------------------------------------------------------------------------------------------------------


#   Creates transition time unit label
#-----------------------------------------------------------------------------------------------------------------------
label5 = Label(master, text="sec")
label5.place(x=235, y=295)
#-----------------------------------------------------------------------------------------------------------------------


#   Main loop - Program sits idle until event occurs (button click, etc.)
#-----------------------------------------------------------------------------------------------------------------------
mainloop()
#-----------------------------------------------------------------------------------------------------------------------
