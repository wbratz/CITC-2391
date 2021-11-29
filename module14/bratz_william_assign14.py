"""
Programmer: William Bratz
Assignment: Module 14 - Assignment
Date Completed: 11/28/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

import tkinter

class TnFlag:
    def __init__(self):
        self.mainWindow = tkinter.Tk()

        # create canvas widget
        self.canvas = tkinter.Canvas(self.mainWindow, width=640, height=400)

        # main part of flag
        self.canvas.create_rectangle(10, 8, 639, 399, fill='#BA0101')

        # blue part
        self.canvas.create_rectangle(600, 8, 639, 399, fill='#003366')

        # white part
        self.canvas.create_rectangle(590, 8, 600, 399, fill='#FFFFFF')

        # draw circle
        self.canvas.create_oval(177, 72, 428, 321, fill="#003366", outline='#FFFFFF', width=6)

        # create stars
        left_star = [203, 120, 235, 118, 248, 85, 262, 119, 299, 120, 270, 144, 280, 178, 248, 160, 217, 178, 226, 144]
        right_star = [309, 179, 351, 177, 366, 138, 381, 177, 423, 180, 390, 204, 401, 245, 366, 224, 331, 245, 341, 204]
        bottom_star = [196, 221, 245, 219, 262, 178, 281, 218, 331, 222, 293, 248, 305, 290, 263, 267, 222, 290, 234, 249]

        self.canvas.create_polygon(left_star, fill='#FFFFFF', width=4)
        self.canvas.create_polygon(right_star, fill='#FFFFFF', width=4)
        self.canvas.create_polygon(bottom_star, fill='#FFFFFF', width=4)
        
        # pack canvas
        self.canvas.pack()

        tkinter.mainloop()


myGui = TnFlag()
