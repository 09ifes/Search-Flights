from tkinter import *
from flight_search import *
from tkinter import ttk


class SearchUI:
    def __init__(self):
        """Initializes and configures the window, and executes flight search ui method"""
        self.window = Tk()
        self.window.title('Flights')
        self.window.config(padx=50, pady=50)
        self.flight_search_ui()

    '''For the 'click' functions, when an input box is clicked, placeholder content gets removed'''
    def click1(self,event):
        self.from_location.configure(state=NORMAL)
        self.from_location.delete(0, END)
        self.from_location.config(foreground='black')
        self.from_location.unbind('<Button-1>', self.click_1)

    def click2(self,event):
        self.to_location.configure(state=NORMAL)
        self.to_location.delete(0, END)
        self.to_location.config(foreground='black')
        self.to_location.unbind('<Button-1>', self.click_2)

    def click3(self,event):
        self.from_date.configure(state=NORMAL)
        self.from_date.delete(0, END)
        self.from_date.config(foreground='black')
        self.from_date.unbind('<Button-1>', self.click_3)

    def click4(self,event):
        self.to_date.configure(state=NORMAL)
        self.to_date.delete(0, END)
        self.to_date.config(foreground='black')
        self.to_date.unbind('<Button-1>', self.click_4)


    def flight_search_ui(self):
        '''Creates the input fields and overall UI'''
        self.from_location = Entry(width=20, foreground='grey')
        self.from_location.grid(row=0, column=0, padx=10, pady=10, ipady=2)
        self.from_location.insert(END, string='Departure')
        self.click_1 = self.from_location.bind('<Button-1>', self.click1)

        self.to_location = Entry(width=20, foreground='grey')
        self.to_location.grid(row=0, column=1, padx=10, pady=10, ipady=2)
        self.to_location.insert(END, string='Destination')
        self.click_2 = self.to_location.bind('<Button-1>', self.click2)

        self.from_date = Entry(width=20, foreground='grey')
        self.from_date.grid(row=1, column=0, padx=10, pady=10, ipady=2)
        self.from_date.insert(END,string='From: e.g. 01/01/2000')
        self.click_3 = self.from_date.bind('<Button-1>', self.click3)

        self.to_date = Entry(width=20, foreground='grey')
        self.to_date.grid(row=1, column=1, padx=10, pady=10, ipady=2)
        self.to_date.insert(END, string='To: e.g. 01/01/2000')
        self.click_4 = self.to_date.bind('<Button-1>', self.click4)

        self.passengers = ttk.Combobox(values=[1,2,3,4,5,6,7,8], width=17)
        self.passengers.insert(0, "Passengers")
        self.passengers.grid(row=2, column=0, padx=10, pady=10)

        self.travel_class = ttk.Combobox(values=['Economy', 'Business', 'First Class'], width=17)
        self.travel_class.insert(0, "Travel Class")
        self.travel_class.grid(row=2, column=1, padx=10, pady=10)

        self.search_button = Button(text='Search Flights', command=self.send_data)
        self.search_button.grid(row=3, column=0, columnspan=2)

        self.window.mainloop()

    def send_data(self):
        '''Retrieves the inputted search parameters and passes to the flight search function'''
        departure = self.from_location.get()
        destination = self.to_location.get()
        from_date = self.from_date.get()
        to_date = self.to_date.get()
        passengers = self.passengers.get()
        travel_class = self.travel_class.get()
        for widget in self.window.winfo_children():
            widget.destroy()             # Destroys current window so that new window can be created to display results
        flight_srch = FlightSearch(departure, destination, from_date, to_date, passengers, travel_class, self.window)
        '''Subsequent code execution takes place in flight_search.py'''

















