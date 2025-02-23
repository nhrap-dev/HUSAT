#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Oct 28, 2019 04:52:39 PM PDT  platform: Windows NT

import sys,utility

try:
    import Tkinter as tk
#     from Tkinter import filedialog
except ImportError:
    import tkinter as tk
#     from Tkinter import filedialog

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from tkinter import *
import HAST_PreProcess_GUI_support

val = None
root = None
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    # utility.popupmsg('1')
    HAST_PreProcess_GUI_support.set_Tk_var()
    # utility.popupmsg('2')
    top = Toplevel1 (root)
    # utility.popupmsg('1')
    HAST_PreProcess_GUI_support.init(root, top)
    root.mainloop()

w = None
w_win = None
rt = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    HAST_PreProcess_GUI_support.set_Tk_var()
    top = Toplevel1 (w)
    HAST_PreProcess_GUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("710x612+450+112")
        top.title("HAST Prototype 1.0 - Pre-Processing")
        top.configure(background="#87CEFA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.SelectInput = tk.Button(top)
        self.SelectInput.place(relx=0.915, rely=0.768, height=24, width=24)
        self.SelectInput.configure(activebackground="#ececec")
        self.SelectInput.configure(activeforeground="#000000")
        self.SelectInput.configure(background="#87CEFA")
        self.SelectInput.configure(command=HAST_PreProcess_GUI_support.browse_button)
        self.SelectInput.configure(disabledforeground="#a3a3a3")
        self.SelectInput.configure(foreground="#000000")
        self.SelectInput.configure(highlightbackground="#d9d9d9")
        self.SelectInput.configure(highlightcolor="black")
        self.SelectInput.configure(pady="0")

        self.RequiredFields = tk.LabelFrame(top)
        self.RequiredFields.place(relx=0.0, rely=0.016, relheight=0.727, relwidth=0.479)
        self.RequiredFields.configure(relief='groove')
        self.RequiredFields.configure(foreground="black")
        self.RequiredFields.configure(text='''Required Input Fields''')
        self.RequiredFields.configure(background="#87CEFA")
        self.RequiredFields.configure(highlightbackground="#d9d9d9")
        self.RequiredFields.configure(highlightcolor="black")

        self.Longitude = tk.Label(self.RequiredFields)
        self.Longitude.place(relx=0.029, rely=0.067, height=26, width=82, bordermode='ignore')
        self.Longitude.configure(activebackground="#f9f9f9")
        self.Longitude.configure(activeforeground="black")
        self.Longitude.configure(anchor='w')
        self.Longitude.configure(background="#87CEFA")
        self.Longitude.configure(disabledforeground="#a3a3a3")
        self.Longitude.configure(foreground="#000000")
        self.Longitude.configure(highlightbackground="#d9d9d9")
        self.Longitude.configure(highlightcolor="black")
        self.Longitude.configure(text='''Longitude*:''')

        self.LongitudeEntry = tk.Entry(self.RequiredFields)
        self.LongitudeEntry.place(relx=0.706, rely=0.067, height=24, relwidth=0.276, bordermode='ignore')
        self.LongitudeEntry.configure(background="white")
        self.LongitudeEntry.configure(disabledforeground="#a3a3a3")
        self.LongitudeEntry.configure(font="TkFixedFont")
        self.LongitudeEntry.configure(foreground="#000000")
        self.LongitudeEntry.configure(highlightbackground="#d9d9d9")
        self.LongitudeEntry.configure(highlightcolor="black")
        self.LongitudeEntry.configure(insertbackground="black")
        self.LongitudeEntry.configure(selectbackground="#c4c4c4")
        self.LongitudeEntry.configure(selectforeground="black")

        self.Latitude = tk.Label(self.RequiredFields)
        self.Latitude.place(relx=0.029, rely=0.135, height=26, width=66, bordermode='ignore')
        self.Latitude.configure(activebackground="#f9f9f9")
        self.Latitude.configure(activeforeground="black")
        self.Latitude.configure(anchor='w')
        self.Latitude.configure(background="#87CEFA")
        self.Latitude.configure(disabledforeground="#a3a3a3")
        self.Latitude.configure(foreground="#000000")
        self.Latitude.configure(highlightbackground="#d9d9d9")
        self.Latitude.configure(highlightcolor="black")
        self.Latitude.configure(text='''Latitude*:''')

        self.LatitudeEntry = tk.Entry(self.RequiredFields)
        self.LatitudeEntry.place(relx=0.706, rely=0.135, height=24, relwidth=0.276, bordermode='ignore')
        self.LatitudeEntry.configure(background="white")
        self.LatitudeEntry.configure(disabledforeground="#a3a3a3")
        self.LatitudeEntry.configure(font="TkFixedFont")
        self.LatitudeEntry.configure(foreground="#000000")
        self.LatitudeEntry.configure(highlightbackground="#d9d9d9")
        self.LatitudeEntry.configure(highlightcolor="black")
        self.LatitudeEntry.configure(insertbackground="black")
        self.LatitudeEntry.configure(selectbackground="#c4c4c4")
        self.LatitudeEntry.configure(selectforeground="black")

        self.SOID = tk.Label(self.RequiredFields)
        self.SOID.place(relx=0.029, rely=0.202, height=26, width=166, bordermode='ignore')
        self.SOID.configure(activebackground="#f9f9f9")
        self.SOID.configure(activeforeground="black")
        self.SOID.configure(anchor='w')
        self.SOID.configure(background="#87CEFA")
        self.SOID.configure(disabledforeground="#a3a3a3")
        self.SOID.configure(foreground="#000000")
        self.SOID.configure(highlightbackground="#d9d9d9")
        self.SOID.configure(highlightcolor="black")
        self.SOID.configure(text='''Specific Occupancy Id*:''')

        self.BuildingArea = tk.Label(self.RequiredFields)
        self.BuildingArea.place(relx=0.029, rely=0.27, height=26, width=106, bordermode='ignore')
        self.BuildingArea.configure(activebackground="#f9f9f9")
        self.BuildingArea.configure(activeforeground="black")
        self.BuildingArea.configure(anchor='w')
        self.BuildingArea.configure(background="#87CEFA")
        self.BuildingArea.configure(disabledforeground="#a3a3a3")
        self.BuildingArea.configure(foreground="#000000")
        self.BuildingArea.configure(highlightbackground="#d9d9d9")
        self.BuildingArea.configure(highlightcolor="black")
        self.BuildingArea.configure(text='''Building Area*:''')

        self.BuildingValue = tk.Label(self.RequiredFields)
        self.BuildingValue.place(relx=0.029, rely=0.337, height=26, width=116, bordermode='ignore')
        self.BuildingValue.configure(activebackground="#f9f9f9")
        self.BuildingValue.configure(activeforeground="black")
        self.BuildingValue.configure(anchor='w')
        self.BuildingValue.configure(background="#87CEFA")
        self.BuildingValue.configure(disabledforeground="#a3a3a3")
        self.BuildingValue.configure(foreground="#000000")
        self.BuildingValue.configure(highlightbackground="#d9d9d9")
        self.BuildingValue.configure(highlightcolor="black")
        self.BuildingValue.configure(text='''Building Value*:''')

        self.HUSBT = tk.Label(self.RequiredFields)
        self.HUSBT.place(relx=0.029, rely=0.472, height=26, width=226, bordermode='ignore')
        self.HUSBT.configure(activebackground="#f9f9f9")
        self.HUSBT.configure(activeforeground="black")
        self.HUSBT.configure(anchor='w')
        self.HUSBT.configure(background="#87CEFA")
        self.HUSBT.configure(disabledforeground="#a3a3a3")
        self.HUSBT.configure(foreground="#000000")
        self.HUSBT.configure(highlightbackground="#d9d9d9")
        self.HUSBT.configure(highlightcolor="black")
        self.HUSBT.configure(text='''Hurricane Specific Building Type*:''')

        self.BuildingAreaEntry = tk.Entry(self.RequiredFields)
        self.BuildingAreaEntry.place(relx=0.706, rely=0.27, height=24, relwidth=0.276, bordermode='ignore')
        self.BuildingAreaEntry.configure(background="white")
        self.BuildingAreaEntry.configure(disabledforeground="#a3a3a3")
        self.BuildingAreaEntry.configure(font="TkFixedFont")
        self.BuildingAreaEntry.configure(foreground="#000000")
        self.BuildingAreaEntry.configure(highlightbackground="#d9d9d9")
        self.BuildingAreaEntry.configure(highlightcolor="black")
        self.BuildingAreaEntry.configure(insertbackground="black")
        self.BuildingAreaEntry.configure(selectbackground="#c4c4c4")
        self.BuildingAreaEntry.configure(selectforeground="black")

        self.BuildingValueEntry = tk.Entry(self.RequiredFields)
        self.BuildingValueEntry.place(relx=0.706, rely=0.337, height=24, relwidth=0.276, bordermode='ignore')
        self.BuildingValueEntry.configure(background="white")
        self.BuildingValueEntry.configure(disabledforeground="#a3a3a3")
        self.BuildingValueEntry.configure(font="TkFixedFont")
        self.BuildingValueEntry.configure(foreground="#000000")
        self.BuildingValueEntry.configure(highlightbackground="#d9d9d9")
        self.BuildingValueEntry.configure(highlightcolor="black")
        self.BuildingValueEntry.configure(insertbackground="black")
        self.BuildingValueEntry.configure(selectbackground="#c4c4c4")
        self.BuildingValueEntry.configure(selectforeground="black")

        self.HUSBTEntry = tk.Entry(self.RequiredFields)
        self.HUSBTEntry.place(relx=0.706, rely=0.472, height=24, relwidth=0.276, bordermode='ignore')
        self.HUSBTEntry.configure(background="white")
        self.HUSBTEntry.configure(disabledforeground="#a3a3a3")
        self.HUSBTEntry.configure(font="TkFixedFont")
        self.HUSBTEntry.configure(foreground="#000000")
        self.HUSBTEntry.configure(highlightbackground="#d9d9d9")
        self.HUSBTEntry.configure(highlightcolor="black")
        self.HUSBTEntry.configure(insertbackground="black")
        self.HUSBTEntry.configure(selectbackground="#c4c4c4")
        self.HUSBTEntry.configure(selectforeground="black")

        self.SOIDEntry = tk.Entry(self.RequiredFields)
        self.SOIDEntry.place(relx=0.706, rely=0.202, height=24, relwidth=0.276, bordermode='ignore')
        self.SOIDEntry.configure(background="white")
        self.SOIDEntry.configure(disabledforeground="#a3a3a3")
        self.SOIDEntry.configure(font="TkFixedFont")
        self.SOIDEntry.configure(foreground="#000000")
        self.SOIDEntry.configure(highlightbackground="#d9d9d9")
        self.SOIDEntry.configure(highlightcolor="black")
        self.SOIDEntry.configure(insertbackground="black")
        self.SOIDEntry.configure(selectbackground="#c4c4c4")
        self.SOIDEntry.configure(selectforeground="black")

        self.ContentValue = tk.Label(self.RequiredFields)
        self.ContentValue.place(relx=0.029, rely=0.404, height=26, width=116, bordermode='ignore')
        self.ContentValue.configure(activebackground="#f9f9f9")
        self.ContentValue.configure(activeforeground="black")
        self.ContentValue.configure(anchor='w')
        self.ContentValue.configure(background="#87CEFA")
        self.ContentValue.configure(disabledforeground="#a3a3a3")
        self.ContentValue.configure(foreground="#000000")
        self.ContentValue.configure(highlightbackground="#d9d9d9")
        self.ContentValue.configure(highlightcolor="black")
        self.ContentValue.configure(text='''Content Value*:''')

        self.ContentValueEntry = tk.Entry(self.RequiredFields)
        self.ContentValueEntry.place(relx=0.706, rely=0.404, height=24, relwidth=0.276, bordermode='ignore')
        self.ContentValueEntry.configure(background="white")
        self.ContentValueEntry.configure(disabledforeground="#a3a3a3")
        self.ContentValueEntry.configure(font="TkFixedFont")
        self.ContentValueEntry.configure(foreground="#000000")
        self.ContentValueEntry.configure(highlightbackground="#d9d9d9")
        self.ContentValueEntry.configure(highlightcolor="black")
        self.ContentValueEntry.configure(insertbackground="black")
        self.ContentValueEntry.configure(selectbackground="#c4c4c4")
        self.ContentValueEntry.configure(selectforeground="black")

        self.OptionalFields = tk.LabelFrame(top)
        self.OptionalFields.place(relx=0.479, rely=0.016, relheight=0.727, relwidth=0.515)
        self.OptionalFields.configure(relief='groove')
        self.OptionalFields.configure(foreground="black")
        self.OptionalFields.configure(text='''Optional Fields''')
        self.OptionalFields.configure(background="#87CEFA")
        self.OptionalFields.configure(highlightbackground="#d9d9d9")
        self.OptionalFields.configure(highlightcolor="black")

        self.TerrainID = tk.Label(self.OptionalFields)
        self.TerrainID.place(relx=0.027, rely=0.135, height=26, width=136, bordermode='ignore')
        self.TerrainID.configure(activebackground="#f9f9f9")
        self.TerrainID.configure(activeforeground="black")
        self.TerrainID.configure(anchor='w')
        self.TerrainID.configure(background="#87CEFA")
        self.TerrainID.configure(disabledforeground="#a3a3a3")
        self.TerrainID.configure(foreground="#000000")
        self.TerrainID.configure(highlightbackground="#d9d9d9")
        self.TerrainID.configure(highlightcolor="black")
        self.TerrainID.configure(text='''TerrainID:''')

        self.TerrainIDEntry = tk.Entry(self.OptionalFields)
        self.TerrainIDEntry.place(relx=0.628, rely=0.135, height=24, relwidth=0.257, bordermode='ignore')
        self.TerrainIDEntry.configure(background="white")
        self.TerrainIDEntry.configure(disabledforeground="#a3a3a3")
        self.TerrainIDEntry.configure(font="TkFixedFont")
        self.TerrainIDEntry.configure(foreground="#000000")
        self.TerrainIDEntry.configure(highlightbackground="#d9d9d9")
        self.TerrainIDEntry.configure(highlightcolor="black")
        self.TerrainIDEntry.configure(insertbackground="black")
        self.TerrainIDEntry.configure(selectbackground="#c4c4c4")
        self.TerrainIDEntry.configure(selectforeground="black")

        self.WBIDEntry = tk.Entry(self.OptionalFields)
        self.WBIDEntry.place(relx=0.628, rely=0.202, height=24, relwidth=0.257, bordermode='ignore')
        self.WBIDEntry.configure(background="white")
        self.WBIDEntry.configure(disabledforeground="#a3a3a3")
        self.WBIDEntry.configure(font="TkFixedFont")
        self.WBIDEntry.configure(foreground="#000000")
        self.WBIDEntry.configure(highlightbackground="#d9d9d9")
        self.WBIDEntry.configure(highlightcolor="black")
        self.WBIDEntry.configure(insertbackground="black")
        self.WBIDEntry.configure(selectbackground="#c4c4c4")
        self.WBIDEntry.configure(selectforeground="black")

        self.WBID = tk.Label(self.OptionalFields)
        self.WBID.place(relx=0.027, rely=0.202, height=26, width=136, bordermode='ignore')
        self.WBID.configure(activebackground="#f9f9f9")
        self.WBID.configure(activeforeground="black")
        self.WBID.configure(anchor='w')
        self.WBID.configure(background="#87CEFA")
        self.WBID.configure(disabledforeground="#a3a3a3")
        self.WBID.configure(foreground="#000000")
        self.WBID.configure(highlightbackground="#d9d9d9")
        self.WBID.configure(highlightcolor="black")
        self.WBID.configure(text='''wbID:''')

        self.CensusBlockIDLabel = tk.Label(self.OptionalFields)
        self.CensusBlockIDLabel.place(relx=0.027, rely=0.067, height=26, width=136, bordermode='ignore')
        self.CensusBlockIDLabel.configure(activebackground="#f9f9f9")
        self.CensusBlockIDLabel.configure(activeforeground="black")
        self.CensusBlockIDLabel.configure(anchor='w')
        self.CensusBlockIDLabel.configure(background="#87CEFA")
        self.CensusBlockIDLabel.configure(disabledforeground="#a3a3a3")
        # self.CensusBlockIDLabel.configure(foreground="#000000")
        # self.CensusBlockIDLabel.configure(highlightbackground="#d9d9d9")
        # self.CensusBlockIDLabel.configure(highlightcolor="black")
        self.CensusBlockIDLabel.configure(foreground="#000000")
        self.CensusBlockIDLabel.configure(highlightbackground="#d9d9d9")
        self.CensusBlockIDLabel.configure(highlightcolor="black")
        self.CensusBlockIDLabel.configure(text='''Census Block Id:''')

        self.CensusBlockIDEntry = tk.Entry(self.OptionalFields)
        self.CensusBlockIDEntry.place(relx=0.628, rely=0.067, height=24, relwidth=0.257, bordermode='ignore')
        self.CensusBlockIDEntry.configure(background="white")
        self.CensusBlockIDEntry.configure(disabledforeground="#a3a3a3")
        self.CensusBlockIDEntry.configure(font="TkFixedFont")
        self.CensusBlockIDEntry.configure(foreground="#000000")
        self.CensusBlockIDEntry.configure(highlightbackground="#d9d9d9")
        self.CensusBlockIDEntry.configure(highlightcolor="black")
        self.CensusBlockIDEntry.configure(insertbackground="black")
        self.CensusBlockIDEntry.configure(selectbackground="#c4c4c4")
        self.CensusBlockIDEntry.configure(selectforeground="black")

        self.TopoSpeedUpChkbx = tk.Checkbutton(self.OptionalFields)
        self.TopoSpeedUpChkbx.place(relx=0.027, rely=0.27, height=26, width=50, bordermode='ignore')
        self.TopoSpeedUpChkbx.configure(activebackground="#f9f9f9")
        self.TopoSpeedUpChkbx.configure(activeforeground="black")
        self.TopoSpeedUpChkbx.configure(anchor='w')
        self.TopoSpeedUpChkbx.configure(background="#87CEFA")
        self.TopoSpeedUpChkbx.configure(disabledforeground="#a3a3a3")
        self.TopoSpeedUpChkbx.configure(foreground="#70747f")
        self.TopoSpeedUpChkbx.configure(highlightbackground="#d9d9d9")
        self.TopoSpeedUpChkbx.configure(highlightcolor="black")

        self.TopoSpeedUp = tk.Label(self.OptionalFields)
        self.TopoSpeedUp.place(relx=0.087, rely=0.27, height=26, width=105, bordermode='ignore')
        self.TopoSpeedUp.configure(activebackground="#f9f9f9")
        self.TopoSpeedUp.configure(activeforeground="black")
        self.TopoSpeedUp.configure(anchor='w')
        self.TopoSpeedUp.configure(background="#87CEFA")
        self.TopoSpeedUp.configure(disabledforeground="#a3a3a3")
        self.TopoSpeedUp.configure(foreground="#70747f")
        self.TopoSpeedUp.configure(highlightbackground="#d9d9d9")
        self.TopoSpeedUp.configure(highlightcolor="black")
        self.TopoSpeedUp.configure(text='''Topo speedup''')
        
        self.RoofShapeChkbx = tk.Checkbutton(self.OptionalFields)
        self.RoofShapeChkbx.place(relx=0.137, rely=0.404, height=26, width=165, bordermode='ignore')
        self.RoofShapeChkbx.configure(activebackground="#f9f9f9")
        self.RoofShapeChkbx.configure(activeforeground="black")        
        self.RoofShapeChkbx.configure(anchor='w')
        self.RoofShapeChkbx.configure(background="#87CEFA")
        self.RoofShapeChkbx.configure(disabledforeground="#a3a3a3")
        self.RoofShapeChkbx.configure(foreground="#70747f")
        self.RoofShapeChkbx.configure(highlightbackground="#d9d9d9")
        self.RoofShapeChkbx.configure(highlightcolor="black")
        # self.RoofShapeChkbx.configure(text='''Roof Shape:''')

        self.RoofShapelbl = tk.Label(self.OptionalFields)
        self.RoofShapelbl.place(relx=0.197, rely=0.404, height=26, width=165, bordermode='ignore')
        self.RoofShapelbl.configure(activebackground="#f9f9f9")
        self.RoofShapelbl.configure(activeforeground="black")
        self.RoofShapelbl.configure(anchor='w')
        self.RoofShapelbl.configure(background="#87CEFA")
        # self.RoofShapelbl.configure(disabledforeground="#a3a3a3")
        self.RoofShapelbl.configure(foreground="#70747f")
        self.RoofShapelbl.configure(highlightbackground="#d9d9d9")
        self.RoofShapelbl.configure(highlightcolor="black")
        self.RoofShapelbl.configure(text='''Roof Shape''')

        self.TopoSpeedUp_4 = tk.Label(self.OptionalFields)
        self.TopoSpeedUp_4.place(relx=0.137, rely=0.472, height=26, width=165, bordermode='ignore')
        self.TopoSpeedUp_4.configure(activebackground="#f9f9f9")
        self.TopoSpeedUp_4.configure(activeforeground="black")
        self.TopoSpeedUp_4.configure(anchor='w')
        self.TopoSpeedUp_4.configure(background="#87CEFA")
        self.TopoSpeedUp_4.configure(disabledforeground="#a3a3a3")
        self.TopoSpeedUp_4.configure(foreground="#70747f")
        self.TopoSpeedUp_4.configure(highlightbackground="#d9d9d9")
        self.TopoSpeedUp_4.configure(highlightcolor="black")
        self.TopoSpeedUp_4.configure(text='''Sec. Water Resistance:''')

        self.Label4 = tk.Label(self.OptionalFields)
        self.Label4.place(relx=0.027, rely=0.337, height=26, width=199, bordermode='ignore')
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(anchor='w')
        self.Label4.configure(background="#87CEFA")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#70747f")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Wind Building Characteristics''')

        self.Label5 = tk.Label(self.OptionalFields)
        self.Label5.place(relx=0.137, rely=0.539, height=26, width=165, bordermode='ignore')
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(anchor='w')
        self.Label5.configure(background="#87CEFA")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#70747f")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Roof deck attachment:''')

        self.Label6 = tk.Label(self.OptionalFields)
        self.Label6.place(relx=0.137, rely=0.607, height=26, width=165, bordermode='ignore')
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(anchor='w')
        self.Label6.configure(background="#87CEFA")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#70747f")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Roof to wall connection:''')

        self.Label7 = tk.Label(self.OptionalFields)
        self.Label7.place(relx=0.027, rely=0.674, height=26, width=180, bordermode='ignore')
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(anchor='w')
        self.Label7.configure(background="#87CEFA")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#70747f")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Garage doors:''')

        self.Label8 = tk.Label(self.OptionalFields)
        self.Label8.place(relx=0.027, rely=0.742, height=26, width=180, bordermode='ignore')
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(anchor='w')
        self.Label8.configure(background="#87CEFA")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#70747f")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Shutters:''')

        self.Label9 = tk.Label(self.OptionalFields)
        self.Label9.place(relx=0.027, rely=0.809, height=26, width=180, bordermode='ignore')
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(anchor='w')
        self.Label9.configure(background="#87CEFA")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#70747f")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Reinforced Masonry:''')

        self.Label9_1 = tk.Label(self.OptionalFields)
        self.Label9_1.place(relx=0.027, rely=0.876, height=26, width=180, bordermode='ignore')
        self.Label9_1.configure(activebackground="#f9f9f9")
        self.Label9_1.configure(activeforeground="black")
        self.Label9_1.configure(anchor='w')
        self.Label9_1.configure(background="#87CEFA")
        self.Label9_1.configure(disabledforeground="#a3a3a3")
        self.Label9_1.configure(foreground="#70747f")
        self.Label9_1.configure(highlightbackground="#d9d9d9")
        self.Label9_1.configure(highlightcolor="black")
        self.Label9_1.configure(text='''IBC Continuous Load Path:''')

        self.Run = tk.Button(top)
        self.Run.place(relx=0.296, rely=0.931, height=33, width=90)
        self.Run.configure(activebackground="#ececec")
        self.Run.configure(activeforeground="#000000")
        self.Run.configure(background="#87CEFA")
        self.Run.configure(command=HAST_PreProcess_GUI_support.analyze)
        self.Run.configure(disabledforeground="#a3a3a3")
        self.Run.configure(foreground="#000000")
        self.Run.configure(highlightbackground="#d9d9d9")
        self.Run.configure(highlightcolor="black")
        self.Run.configure(pady="0")
        self.Run.configure(text='''Process''')

        self.QuitButton = tk.Button(top)
        self.QuitButton.place(relx=0.577, rely=0.931, height=33, width=90)
        self.QuitButton.configure(activebackground="#ececec")
        self.QuitButton.configure(activeforeground="#000000")
        self.QuitButton.configure(background="#87CEFA")
        self.QuitButton.configure(command=HAST_PreProcess_GUI_support.Exit)
        self.QuitButton.configure(disabledforeground="#a3a3a3")
        self.QuitButton.configure(foreground="#000000")
        self.QuitButton.configure(highlightbackground="#d9d9d9")
        self.QuitButton.configure(highlightcolor="black")
        self.QuitButton.configure(pady="0")
        self.QuitButton.configure(text='''Exit''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.014, rely=0.67, height=26, width=214)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#87CEFA")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''* Indicates a required field.''')

        self.MainScreenButton = tk.Button(top)
        self.MainScreenButton.place(relx=0.437, rely=0.931, height=33, width=90)
        self.MainScreenButton.configure(activebackground="#ececec")
        self.MainScreenButton.configure(activeforeground="#000000")
        self.MainScreenButton.configure(background="#87CEFA")
        self.MainScreenButton.configure(command=HAST_PreProcess_GUI_support.MainScreen)
        self.MainScreenButton.configure(disabledforeground="#a3a3a3")
        self.MainScreenButton.configure(foreground="#000000")
        self.MainScreenButton.configure(highlightbackground="#d9d9d9")
        self.MainScreenButton.configure(highlightcolor="black")
        self.MainScreenButton.configure(pady="0")
        self.MainScreenButton.configure(text='''Main Menu''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.014, rely=0.768, height=26, width=87)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(anchor='nw')
        self.Label2.configure(background="#87CEFA")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Select Input:''')

        self.InputEntry = tk.Entry(top)
        self.InputEntry.place(relx=0.141, rely=0.768,height=24, relwidth=0.766)
        self.InputEntry.configure(background="white")
        self.InputEntry.configure(disabledforeground="#a3a3a3")
        self.InputEntry.configure(font="TkFixedFont")
        self.InputEntry.configure(foreground="#000000")
        self.InputEntry.configure(highlightbackground="#d9d9d9")
        self.InputEntry.configure(highlightcolor="black")
        self.InputEntry.configure(insertbackground="black")
        self.InputEntry.configure(selectbackground="#c4c4c4")
        self.InputEntry.configure(selectforeground="black")
        self.InputEntry.configure(textvariable=HAST_PreProcess_GUI_support.FileText)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.007, rely=0.833, relheight=0.082
                , relwidth=0.951)
        self.Message1.configure(anchor='nw')
        self.Message1.configure(background="#87CEFA")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(text='''The pre-processing tool provides surface roughness (TerrainID) based on location and specific wind building IDs (wbID) based on Hurricane Specific Building Type (huSBT) if not provided by the user.''')
        self.Message1.configure(width=675)

if __name__ == '__main__':
    vp_start_gui()






