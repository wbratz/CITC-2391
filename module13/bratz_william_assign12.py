"""
Programmer: William Bratz
Assignment: Module 13 - Assignment
Date Completed: 11/16/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

"""
Programmer: William Bratz
Assignment: Module 12 - Lab
Date Completed: 11/16/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

import tkinter

class MilesPerGallonCalculatorGUI:
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.geometry('500x200')
        # Three Frames to group widgets
        self.top_frame = tkinter.Frame()
        self.mid_top = tkinter.Frame()
        self.mid_frame = tkinter.Frame()
        self.mid_bottom = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # create top frame widgets
        self.top_label = tkinter.Label(self.top_frame,
            text="Calculate Miles Per Gallon")

        #pack top frame
        self.top_label.pack(side='left')

        #mid-top frame widgets
        self.gallons_label = tkinter.Label(self.mid_top,
            text='Enter gallons of gas the car holds:')

        self.gallons_entry = tkinter.Entry(self.mid_top, 
            width=10)

        # pack mid-top
        self.gallons_label.pack(side='left')
        self.gallons_entry.pack(side='left')

        #middle frame widgets
        self.miles_label = tkinter.Label(self.mid_frame, 
            text='Enter the miles the car can travel on a tank of gas')
        
        self.miles_entry = tkinter.Entry(self.mid_frame, 
            width=10)
        
        #pack middle frame
        self.miles_label.pack(side='left')
        self.miles_entry.pack(side='left')

        # stringvar to assocate with output label
        self.mpg = tkinter.StringVar()

        # mpg label so there isn't just a hole in the application
        # make label and assocate it with the stringvar
        # any value stored in stringvar will be displayed
        self.mpg_text_label = tkinter.Label(self.mid_bottom, text="Calculated MPG:")
        self.mpg_label = tkinter.Label(self.mid_bottom, 
            textvariable=self.mpg, pady=20)

        # pack middle-bottom frame
        self.mpg_text_label.pack(side='left')
        self.mpg_label.pack(side='left')

        #create button widget
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Calculate MPG', command=self.calculate_mpg)

        # pack buttons
        self.calc_button.pack(side='left')

        # pack frames
        self.top_frame.pack()
        self.mid_top.pack()
        self.mid_frame.pack()
        self.mid_bottom.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def calculate_mpg(self):
        mpg = int(self.miles_entry.get())/int(self.gallons_entry.get())

        self.mpg.set(mpg)

mpg_calc = MilesPerGallonCalculatorGUI()