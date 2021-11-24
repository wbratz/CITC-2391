"""
Programmer: William Bratz
Assignment: Module 14 - Lab
Date Completed: 11/23/21
Course: CITC 2391 - C01
Instructor: Martin Bell
"""

import tkinter
import tkinter.messagebox

class JoesAutomotiveGUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tkinter.Tk()

        # Set window size
        self.main_window.geometry("300x300")

        # Create three frames. One for the checkbuttons
        # one for the radio buttons
        # and another for the regular Button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
       
        # Create three IntVar objects to use with
        # the Checkbuttons.
        self.oil_change_value = tkinter.IntVar()
        self.lube_job_value = tkinter.IntVar()
        self.radiator_flush_value = tkinter.IntVar()
        self.transmission_flush_value = tkinter.IntVar()
        self.inspection_value = tkinter.IntVar()
        self.muffler_replacement_value = tkinter.IntVar()
        self.tire_rotation_value = tkinter.IntVar()

      
        # Set the intVar objects to 0.
        self.oil_change_value.set(0)
        self.lube_job_value.set(0)
        self.radiator_flush_value.set(0)
        self.transmission_flush_value.set(0)
        self.inspection_value.set(0)
        self.muffler_replacement_value.set(0)
        self.tire_rotation_value.set(0)

        # Create the Checkbutton widgets in the top_frame.
        self.oil_change = tkinter.Checkbutton(self.top_frame, text='Oil Change - $30.00', variable=self.oil_change_value)
        self.lube_job = tkinter.Checkbutton(self.top_frame, text='Lube Job - $20.00', variable=self.lube_job_value)
        self.radiator_flush = tkinter.Checkbutton(self.top_frame, text='Radiator Flush - $40.00', variable=self.radiator_flush_value)
        self.transmission_flush = tkinter.Checkbutton(self.top_frame, text='Transmission Flush - $100.00', variable=self.transmission_flush_value)
        self.inspection = tkinter.Checkbutton(self.top_frame, text='Inspection - $35.00', variable=self.inspection_value)
        self.muffler_replacement = tkinter.Checkbutton(self.top_frame, text='Muffler Replacement - $200.00', variable=self.muffler_replacement_value)
        self.tire_rotation = tkinter.Checkbutton(self.top_frame, text='Tire Rotation - $20.00', variable=self.tire_rotation_value)

        # Pack the Checkbuttons.
        self.oil_change.pack()
        self.lube_job.pack()
        self.radiator_flush.pack()
        self.transmission_flush.pack()
        self.inspection.pack()
        self.muffler_replacement.pack()
        self.tire_rotation.pack()

        # Create label for the car wash radio buttons
        self.car_wash_label = tkinter.Label(self.mid_frame, text='Would you like a Car Wash?')

        # Create the car wash radio buttons
        self.car_wash_var = tkinter.IntVar()

        # create widgets
        self.car_wash_radio1 = tkinter.Radiobutton(self.mid_frame, text='Yes', variable=self.car_wash_var, value=1)
        self.car_wash_radio2 = tkinter.Radiobutton(self.mid_frame, text='No', variable=self.car_wash_var, value=2)

        self.car_wash_label.pack()
        self.car_wash_radio1.pack()
        self.car_wash_radio2.pack()

        # Create an OK button and a Quit button.
        self.ok_button = tkinter.Button(self.bottom_frame, text='Display Charges', command=self.display_charges)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        # Pack the Buttons.
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        # Pack the frames.
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
      
        # Start the mainloop.
        tkinter.mainloop()
        # The show_choice method is the callback function for the
        # OK button.
  
    def display_charges(self):
        # Create a message string.
        self.message = 'Your total charges = '
        # Determine which Checkbuttons are selected and
        # build the message string accordingly.

        charges = 0
        
        if self.oil_change_value.get() == 1:
            charges += 30
        if self.lube_job_value.get() == 1:
            charges += 20
        if self.radiator_flush_value.get() == 1:
            charges += 40
        if self.transmission_flush_value.get() == 1:
            charges += 40
        if self.inspection_value.get() == 1:
            charges += 35
        if self.muffler_replacement_value.get() == 1:
            charges += 200
        if self.tire_rotation_value.get() == 1:
            charges += 20

        self.message += "$"+str(charges)+".00\n"

        if self.car_wash_var.get() == 1:
            self.message += 'Free car wash was accepted'
        if self.car_wash_var.get() == 2:
            self.message += 'Free car wash was declined'

        # Display the message in an info dialog box.
        tkinter.messagebox.showinfo('Total Charges', self.message)
        # Create an instance of the MyGUI class.

automotive_gui = JoesAutomotiveGUI()