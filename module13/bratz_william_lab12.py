"""
Programmer: William Bratz
Assignment: Module 12 - Lab
Date Completed: 11/16/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

import tkinter

class ShowInfoGui:
    def __init__(self):

        self.main_window = tkinter.Tk()

        self.main_window.title("Show Info")
        #set windo dimensions
        self.main_window.geometry("300x200")

        # two Frames to group widgets
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # stringvar to assocate with output label
        self.value = tkinter.StringVar()

        # create top frame widgets
        # make label and assocate it with the stringvar
        # any value stored in stringvar will be displayed
        self.info_label = tkinter.Label(self.top_frame, textvariable=self.value, height=10, padx=10)

        #pack top frame
        self.info_label.pack(side='left')

        #create button widgets
        self.calc_button = tkinter.Button(self.bottom_frame, text = 'Show Info', command=self.show_info)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Exit", command=self.main_window.destroy, width=5)

        # pack buttons
        self.calc_button.pack(side=tkinter.LEFT, padx=25, pady=5)
        self.quit_button.pack(side=tkinter.RIGHT, padx=25, pady=5)

        # pack frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        tkinter.mainloop()

    def show_info(self):
        self.value.set("William Bratz\n527 Old lebanon dirt rd Hermitage TN\n615-210-9939")

kilo_conv = ShowInfoGui()