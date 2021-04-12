import tkinter
from tkinter import StringVar, Frame, Label, Entry, DoubleVar
from Calculator import Calculator
import typing


class Window:
    calculator = Calculator()

    # My window!
    __window: tkinter.Tk = tkinter.Tk()

    # Section for the Price Per Gallon frame of the form
    # StringVar representing the price per gallon
    __ppg: DoubleVar = DoubleVar(value=3.0)
    __ppg_frame: Frame = Frame(__window)
    __ppg_label: Label = Label(__ppg_frame,           text='       PPG: ')
    __ppg_entry: Entry = Entry(__ppg_frame, textvariable=__ppg)

    # Section for the MPGs frame
    # StringVar representing the mileage per gallon
    __mpgs_frame: Frame = Frame(__window)
    __sv_MPGs: DoubleVar = DoubleVar(value=19.0)
    __mpgs_label: Label = Label(__mpgs_frame,         text='    MPGs: ')
    __mpgs_entry: Entry = Entry(__mpgs_frame, textvariable=__sv_MPGs)

    # StringVar representing the distance to be travelled on the trip
    __distance: DoubleVar = DoubleVar(value=1000)
    __distance_frame: Frame = Frame(__window)
    __distance_label: Label = Label(__distance_frame, text='Distance: ')
    __distance_entry: Entry = Entry(__distance_frame, textvariable=__distance)

    # Packs the PPG, MPGs, and distance frames
    def __init__(self):

        # We want the Frames themselves to stack from top to bottom
        # Frame - PPG
        # Frame - MPG
        # Frame - Distance
        frame_orientation: str = 'top'

        # We want the Frames to populate from left to right.
        # Label -> Entry Box
        frame_internal_orientation = 'left'

        # Assemble the price per gallon frame
        self.__ppg_label.pack(side=frame_internal_orientation)
        self.__ppg_entry.pack()
        self.bind_entry_box(self.__ppg_entry)
        self.__ppg_frame.pack(side=frame_orientation)

        # Assemble the MPGs frame
        self.__mpgs_label.pack(side=frame_internal_orientation)
        self.__mpgs_entry.pack()
        self.bind_entry_box(self.__mpgs_entry)
        self.__mpgs_frame.pack()

        # Assemble the distance entry frame
        self.__distance_label.pack(side=frame_internal_orientation)
        self.__distance_entry.pack()
        self.bind_entry_box(self.__distance_entry)
        self.__distance_frame.pack()

        self.__distance.trace_add('write', callback=self.calculate)

        self.__window.mainloop()

    # Used as a callback for when any of the entry boxes have their values changed
    def calculate(self, var, index, mode) -> float:
        try:
            ppg = float(self.__ppg.get())
            mpg = float(self.__sv_MPGs.get())
            distance: float = float(self.__distance.get())
            cost = self.calculator.calculate_cost(ppg, mpg, distance)
            print('The cost is: $ ', cost)

            return cost

        except tkinter.TclError:
            print('One of the boxes contains something that is not an number!')
            return -1


    def bind_entry_box(self, entry: Entry):
        entry.bind('<Return>', lambda x: self.calculate(var=0, index=0, mode=0))