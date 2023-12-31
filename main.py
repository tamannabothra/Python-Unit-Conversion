import sys
import tkinter as tk
from tkinter import *   
import os
from functools import partial
from tkinter import Tk, StringVar , ttk



#Main Window    
root = Tk()
root.title('Converter Menu')
root.geometry("690x200+40+40")
root.config(bg="black")
root.minsize(width=690, height=200)
root.maxsize(width=990, height=500)
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
lbl_title = Label(Top, text="UNIT CONVERTER", font=('times new roman', 16), bg="yellow" , fg="black",width=700)
lbl_title.pack(fill=X)

#Exit button
widget = Button(None, text="Exit ",width = 20,height=1, bg="red", fg="white",font = ("times new roman", 14, "bold"), bd=1, activebackground = "red", activeforeground="black", command=root.destroy).place(x=350,y=100)

def WeightConverter():
        #Factors of conversion from any unit to grams
    factors = {'kg' : 1000, 'hg' : 100, 'dg' : 10, 'g' : 1,'deg' : 0.1, 'cg' : 0.01, 'mg' : 0.001}
    ids = {"Kilogram" : 'kg', "Hectagram" : 'hg', "Decagram" : 'dg', "Decigram" : 'deg', "Kilogram" : 'kg', "gram" : 'g', "centigram" : 'cg', "milligram" : 'mg'}
  
    def convert(amt, frm, to):
        if frm != 'g':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    
    #Window for weight convertoer
    mainframe = Toplevel()
    mainframe.config(bg='black')
    mainframe.minsize(width=495, height=230)
    mainframe.maxsize(width=495, height=230)
    titleLabel = Label (mainframe, text = "Weight Converter", font = ("times new roman", 12, "bold"),bg='yellow', justify = CENTER).grid(column=1,row=1)

    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = ttk.Entry(mainframe, width=20, textvariable=in_amt)
    in_field.grid(row=1, column=2, sticky=(W, E))

    in_select = OptionMenu(mainframe, in_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram") .grid(column=3, row=1, sticky=W)


    ttk.Entry(mainframe, textvariable=out_amt, state="readonly").grid(column=2, row=3, sticky=(W, E))
    in_select = OptionMenu(mainframe, out_unit, "Kilogram","Hectagram","Decagram", "gram", "Decigram","Centigram", "Milligram").grid(column=3, row=3, sticky=W)

    calc_button = Button(mainframe, text="Calculate", bg="skyblue" , fg="black",font = ("times new roman", 14, "bold"), relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command=callback).grid(column=2, row=2, sticky=E)

    for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

    in_field.focus()





def LengthConverter():
        #factor to convert from any unit to meter
    factors = {'nmi' : 1852, 'mi' : 1609.34, 'yd' : 0.9144, 'ft' : 0.3048, 'inch' : 0.0254, 'km' : 1000, 'm' : 1, 'cm' : 0.01, 'mm' : 0.001}
    ids = {"Nautical Miles" : 'nmi', "Miles" : 'mi', "Yards" : 'yd', "Feet" : 'ft', "Inches" : 'inch', "Kilometers" : 'km', "meters" : 'm', "centimeters" : 'cm', "millileters" : 'mm'}

  
    def convert(amt, frm, to):
        if frm != 'm':
            amt = amt * factors[frm]
            return amt / factors[to]
        else:
            return amt / factors[to]

    def callback():
        try:
            amt = float(in_field.get())
        except ValueError:
            out_amt.set('Invalid input')
            return None
        if in_unit.get() == 'Select Unit' or out_unit.get() == 'Select Unit':
            out_amt.set('Input or output unit not chosen')
            return None
        else:
            frm = ids[in_unit.get()]
            to = ids[out_unit.get()]
            out_amt.set(convert(amt, frm, to))

    top = Toplevel()
    top.title("Length Converter")
    top.config(bg="black")
    top.minsize(width=475, height=270)
    top.maxsize(width=475, height=270)

    titleLabel = Label (top, text = "Length Converter", font=('times new roman', 16), bg="yellow" , fg="black").grid(row=1)



    
    fahLabel = Label (top, text = "To :", font = ("times new roman", 18),bg='skyblue', fg = "black")
    fahLabel.grid(row = 4, column = 1, pady = 15, sticky = NW)
    in_amt = StringVar()
    in_amt.set('0')
    out_amt = StringVar()

    in_unit = StringVar()
    out_unit = StringVar()
    in_unit.set('Select Unit')
    out_unit.set('Select Unit')

    in_field = Entry(top, width=20, textvariable=in_amt)
    in_field.grid( column=1,row=3, sticky=(W, E))

    in_select = OptionMenu(top, in_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=2, row=3, sticky=W)

    Entry(top, textvariable=out_amt).grid(column=1, row=6)
    in_select = OptionMenu(top, out_unit, "Nautical Miles", "Miles", "Yards", "Feet", "Inches", "Kilometers", "meters", "centimeters", "millileters").grid(column=2, row=6, sticky=W)

    calc_button = Button(top, text="Calculate",bg="skyblue" , fg="black",font = ("times new roman", 12, "bold"),relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command=callback).grid(column=1, row=7, sticky=E)

    for child in top.winfo_children(): child.grid_configure(padx=2, pady=2)

    in_field.focus()




def TemperatureConverter():
    def convert():
        celTemp = celTempVar.get()
        fahTemp = fahTempVar.get()



        if celTempVar.get() != 0.0:
            celToFah = (celTemp *  9/5 + 32)
            fahTempVar.set(celToFah)

        elif fahTempVar.get() != 0.0:
            fahToCel = ((fahTemp - 32) * (5/9))
            celTempVar.set(fahToCel)

    def reset():
        fahTempVar.set(int(0))
        celTempVar.set(int(0))
    top = Toplevel()
    top.title("Temperature Converter")
    top.config(bg="black")
    top.minsize(width=440, height=290)
    top.maxsize(width=440, height=290)
    
    celTempVar = IntVar()
    celTempVar.set(int(0))
    fahTempVar = IntVar()
    fahTempVar.set(int(0))

    titleLabel = Label (top, text = "Temperature Converter", font=('times new roman', 16), bg="yellow" , fg="black",width=28).grid(column=1,row=1)


    celLabel = Label (top, text = "Celcius:", font = ("times new roman", 18),bg='skyblue', fg = "black")
    celLabel.grid(row = 3, column = 1, pady = 15, sticky = NW)

    fahLabel = Label (top, text = "Fahrenheit:", font = ("times new roman", 18),bg='skyblue', fg = "black")
    fahLabel.grid(row = 4, column = 1, pady = 15, sticky = NW)

    celEntry = Entry (top, width = 10, bd = 1, textvariable = celTempVar)
    celEntry.grid(row = 3, column = 1, pady = 20, sticky = NW, padx = 125 )


    fahEntry = Entry (top, width = 10, bd = 1, textvariable = fahTempVar)
    fahEntry.grid(row = 4, column = 1, pady = 20, sticky = NW, padx = 125 )

    convertButton =Button (top, text = "Convert", bg="yellow" , fg="black",font = ("times new roman", 14, "bold"), relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command = convert)
    convertButton.grid(row = 5, column = 1, ipady = 2, ipadx = 2, pady = 2, sticky = NW)



    resetButton = Button (top, text = "   Reset  ", bg="yellow" , fg="black",font = ("times new roman", 14, "bold"), relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command = reset).place(x=180,y=154)
#area converter
def AreaConverter():
    wind = Toplevel()
    wind.config(bg='black')
    wind.minsize(width=400, height=240)
    wind.maxsize(width=400, height=240)

    meterFactor = {'square meter':1,'square km':1000000,'square rood':1011.7141056,'square cm':0.0001,'square foot':0.09290304 ,
                    'square inch':0.00064516, 'square mile':2589988.110336, 'milimeter':0.000001,'square rod':25.29285264,
                    'square yard':0.83612736, 'square township':93239571.9721, 'square acre':4046.8564224 ,'square are': 100,
                    'square barn':1e-28, 'square hectare':10000, 'square homestead':647497.027584 }



    def convert(x, fromUnit, toUnit):
        if fromVar.get() in meterFactor.keys() and toVar.get() in meterFactor.keys():
            resultxt.delete(0, END)
            result = (float(str(x))*meterFactor[fromUnit])/(meterFactor[toUnit])
            resultxt.insert(0, str(result))
    
    
    
    titleLabel = Label (wind, text = "Area Converter", font = ("times new roman", 12, "bold"),bg='yellow', justify = CENTER).grid(column=1,row=1)

   

    e = Entry(wind)
    e.grid(row = 2, column = 1)
    values = list(meterFactor.keys())

    fromVar = StringVar(wind)
    toVar = StringVar(wind)
    fromVar.set("From Unit")
    toVar.set("To Unit")


    fromOption = OptionMenu(wind, fromVar, *values, command= lambda y: convert(e.get(), fromVar.get() ,toVar.get()))
    fromOption.grid(row=2, column = 2)

    toLabel = Label(wind, text="To : ", font="Arial").grid(row=3, column = 1)
    toOption = OptionMenu(wind, toVar, *values, command= lambda x: convert(e.get(), fromVar.get() ,toVar.get()))
    toOption.grid(row=4, column = 2)

    resultxt = Entry(wind)
    resultxt.grid(row=4, column=1)


widget = Button(root, text="    Temperature Converter   ", bg="white" , fg="black",font = ("times new roman", 14, "bold"), relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command=TemperatureConverter).place(x=0,y=40)

widget = Button(root, text="      Area Converter      ", bg="white" , fg="black",font = ("times new roman", 14, "bold"), relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command=AreaConverter).place(x=260,y=40)

widget = Button(root, text="    Length Converter     ", bg="white" , fg="black",font = ("times new roman", 14, "bold"), relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command=LengthConverter).place(x=100,y=100)

widget = Button(root, text="      Weight Converter      ", bg="white" , fg="black",font = ("times new roman", 14, "bold"), relief = RAISED, bd=1, justify = CENTER, highlightbackground = "red", overrelief = GROOVE, activebackground = "black", activeforeground="blue", command=WeightConverter).place(x=475,y=40)

root.mainloop()