from tkinter import *
from tkinter import ttk
import requests
from flight_details import *
from functools import partial


class ResultsUI:
    def __init__(self, window, flights_list, passengers):
        """Reconstructs and configures window, receives flight data and defines some variables"""
        self.window = window
        self.window.title('Flights')
        self.window.minsize(width=500, height=500)
        self.window.config(padx=50, pady=50)
        self.flight_details_objects = []      # Flight details for each flight instance will be stored as objects here
        self.flights_list = flights_list
        self.passengers = passengers
        self.configure_window()


    def configure_window(self):
        """Configures window incl. scrollbar"""
        self.canvas1 = Canvas(self.window, borderwidth=0)
        self.frame = Frame(self.canvas1)
        self.scrollbar = Scrollbar(orient='vertical', command=self.canvas1.yview)
        self.canvas1.configure(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side='right', fill='y')
        self.canvas1.pack(side='left', fill='both', expand=True)
        self.canvas1.create_window((0, 0), window=self.frame, anchor='nw')
        self.canvas1.bind('<Configure>', self.on_configure)


    def on_configure(self, event):
        self.canvas1.configure(scrollregion=self.canvas1.bbox('all'))


    def flight_pay(self, n):
        """Redirects to third party site to complete the booking"""
        index = n - 1
        payment_url = self.flight_details_objects[index].payment_url
        webbrowser.open(payment_url)


    def back_to_results(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.configure_window()
        self.flight_results_ui()


    def flight_details_ui(self, n):
        """Creates flight details page, and displays the details using the data retrieved from the stored flight
        details object"""
        global logo_1, logo_2        # Made global to avoid garbage collection (image variable data gets lost)
        index = n - 1
        for widget in self.window.winfo_children():
            widget.destroy()

        departure_airport = self.flight_details_objects[index].departure_airport
        destination_airport = self.flight_details_objects[index].destination_airport
        price = self.flight_details_objects[index].price
        from_date = self.flight_details_objects[index].from_date
        to_date = self.flight_details_objects[index].to_date
        depart_time = self.flight_details_objects[index].depart_time
        arrive_time = self.flight_details_objects[index].arrive_time
        departure_airline = self.flight_details_objects[index].departure_airline

        depart_time_ret = self.flight_details_objects[index].depart_time_ret
        arrive_time_ret = self.flight_details_objects[index].arrive_time_ret
        return_airline = self.flight_details_objects[index].return_airline
        airline_code_1 = self.flight_details_objects[index].airline_code_1
        airline_code_2 = self.flight_details_objects[index].airline_code_2
        passengers = self.passengers
        travel_class_1 = self.flight_details_objects[index].travel_class_1
        travel_class_2 = self.flight_details_objects[index].travel_class_2

        logo1_endpoint = f'http://pics.avs.io/90/30/{airline_code_1}.png'      # Endpoints to retrieve logos
        logo2_endpoint = f'http://pics.avs.io/90/30/{airline_code_2}.png'

        logo1_data = requests.get(logo1_endpoint, stream=True)
        logo_1 = PhotoImage(data=logo1_data.content)
        logo2_data = requests.get(logo2_endpoint, stream=True)
        logo_2 = PhotoImage(data=logo2_data.content)

        """Below creates and positions all the components on screen"""
        canvas = Canvas(width=500, height=500, bg='white', highlightthickness=0)

        title = canvas.create_text(250, 20, text=f'Flight {n}', fill='black', font=('Arial', 20, 'bold'))
        dates = canvas.create_text(250, 55, text=f'{from_date}   -   {to_date}', font=('Arial', 10))
        airports = canvas.create_text(250, 105, text=f'{departure_airport} - {destination_airport}', font=('Arial', 15))
        logo1 = canvas.create_image(60, 150, image=logo_1)
        outbound_times = canvas.create_text(250, 150, text=f'{depart_time[0]}:{depart_time[1]} - {arrive_time[0]}:{arrive_time[1]}', fill='black', font=('Arial', 20,))
        departure_airline = canvas.create_text(375, 130, text=f'Airline: {airline_code_1}', font=('Arial', 9))
        passengers1 = canvas.create_text(388, 150, text=f'Passengers: {passengers}', font=('Arial', 9))
        travel_class1 = canvas.create_text(410, 170, text=f'Travel Class: {travel_class_1}', font=('Arial', 9))

        airports_ret = canvas.create_text(250, 250, text=f'{destination_airport} - {departure_airport}', font=('Arial', 15))
        logo2 = canvas.create_image(60, 295, image=logo_2)
        return_times = canvas.create_text(250, 295, text=f'{depart_time_ret[0]}:{depart_time_ret[1]} - {arrive_time_ret[0]}:{arrive_time_ret[1]}', fill='black', font=('Arial', 20,))
        return_airline = canvas.create_text(375, 275, text=f'Airline: {airline_code_2}')
        passengers2 = canvas.create_text(388, 295, text=f'Passengers: {passengers}', font=('Arial', 9))
        travel_class2 = canvas.create_text(410, 315, text=f'Travel Class: {travel_class_1}', font=('Arial', 9))
        price_text = canvas.create_text(250, 380, text=f'£{price}', fill='red', font=('Arial', 20))

        pay_button = Button(canvas, text='Pay Now', command=partial(self.flight_pay, n))
        pay_button.place(x=400, y=360)
        back_button = Button(canvas, text='Back', command=self.back_to_results)
        back_button.place(x=30, y=10)

        canvas.grid(column=0, row=1, pady=10, padx=10)


    def flight_results_ui(self):
        """Uses flight results data to produce and display all the flights, and the associated flight details"""
        for number in range(0, len(self.flights_list)):
            Grid.rowconfigure(self.window, number, weight=1)
        Grid.columnconfigure(self.window, 0, weight=1)

        n = 0
        for flight in self.flights_list:
            n += 1
            departure_airport = flight['flyFrom']
            destination_airport = flight['flyTo']
            price = flight['price']
            from_date = ((flight['route'][0]['local_departure']).split('T')[0]).split('-')
            from_date = f'{from_date[2]}/{from_date[1]}/{from_date[0]}'
            to_date = ((flight['route'][1]['local_departure']).split('T')[0]).split('-')
            to_date = f'{to_date[2]}/{to_date[1]}/{to_date[0]}'
            depart_time = ((flight['route'][0]['local_departure']).split('T')[1].split('.')[0]).split(':')
            arrive_time = ((flight['route'][0]['local_arrival']).split('T')[1].split('.')[0]).split(':')
            departure_airline = flight['route'][0]['airline']
            depart_time_ret = ((flight['route'][1]['local_departure']).split('T')[1].split('.')[0]).split(':')
            arrive_time_ret = ((flight['route'][1]['local_arrival']).split('T')[1].split('.')[0]).split(':')
            return_airline = flight['route'][1]['airline']
            airline_code_1 = flight['route'][0]['airline']
            airline_code_2 = flight['route'][1]['airline']

            flight_details_object = FlightDetails(flight)
            self.flight_details_objects.append(flight_details_object)   # Stores the instances of flight details

            self.canvas = Canvas(self.frame, width=300, height=124, bg='white', highlightthickness=0)
            flight_number = self.canvas.create_text(40, 19, text=f'Flight {n}', font=('Arial', 12, 'bold'))
            outbound_times = self.canvas.create_text(60, 45, text=f'{depart_time[0]}:{depart_time[1]} - {arrive_time[0]}:{arrive_time[1]}', fill='black', font=('Arial', 10, 'bold'))
            airports = self.canvas.create_text(60, 60, text=f'{departure_airport} - {destination_airport}, {departure_airline}', fill='red', font=('Arial', 7,'bold'))
            return_times = self.canvas.create_text(60, 85, text=f'{depart_time_ret[0]}:{depart_time_ret[1]} - {arrive_time_ret[0]}:{arrive_time_ret[1]}', fill='black', font=('Arial', 10, 'bold'))
            airports_ret = self.canvas.create_text(60, 100, text=f'{destination_airport} - {departure_airport}, {return_airline}', fill='red', font=('Arial', 7,'bold'))
            price_text = self.canvas.create_text(220, 60, text=f'£{price}', fill='red', font=('Arial', 15))
            date_range_text = self.canvas.create_text(220, 20, text=f'{from_date} - {to_date}', fill='black', font=('Arial', 10, 'bold'))

            """Button below redirects to flight details ui, variable n is used so that the correct flight details object is referenced"""
            details_button = Button(self.canvas, text='View Details', command=partial(self.flight_details_ui, n))
            details_button.place(x=170, y=80)
            self.canvas.grid(column=0, row=0+n, pady=20)      # Displays and positions the instance of each flight result



        self.window.mainloop()



    ''' Code N/A for now
    
    logo_endpoint1 = f'http://pics.avs.io/30/10/{airline_code_1}.png'
    logo_endpoint2 = f'http://pics.avs.io/30/10/{airline_code_2}.png'
    logo_1_data = requests.get(logo_endpoint1, stream=True)
    logo_2_data = requests.get(logo_endpoint2, stream=True)
    
    img_1 = PhotoImage(data=logo_1_data.content)
    self.img1_canvas = Canvas(self.canvas, width=30, height=10, highlightthickness=0)
    self.img1_canvas.place(x=110, y=50)
    logo_1 = self.img1_canvas.create_image(15, 5, image=img_1)

    img_2 = PhotoImage(data=logo_2_data.content)
    self.img2_canvas = Canvas(self.canvas, width=30, height=10, highlightthickness=0)
    self.img2_canvas.place(x=110, y=90)
    logo_2 = self.img2_canvas.create_image(15, 5, image=img_2)
    
    
    
    
    '''






