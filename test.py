from search_ui import *
from results_ui import *
from tkinter import *
from tkinter import ttk
import requests
from flight_details import *

window = Tk()
window.title('Flights')
window.minsize(width=500,height=500)
window.config(padx=50, pady=50)

logo_endpoint1 = f'http://pics.avs.io/90/30/BA.png'

r = requests.get(logo_endpoint1, stream=True)
logo_1 = PhotoImage(data=r.content)
canvas = Canvas(width=500, height=500, bg='white', highlightthickness=0)

title = canvas.create_text(250, 20, text=f'Flight 1', fill='black', font=('Arial', 20, 'bold'))
dates = canvas.create_text(250, 55, text='23/08/2222   -   25/08/2222', font=('Arial', 10))
airports = canvas.create_text(250, 105, text='Lon - Par', font=('Arial', 15))
logo = canvas.create_image(60, 150, image=logo_1)
outbound_times = canvas.create_text(250, 150, text=f'20:00 - 21:50', fill='black', font=('Arial', 20,))
departure_airline = canvas.create_text(375, 130, text='Airline: BA', font=('Arial', 9))
passengers = canvas.create_text(388, 150, text='Passengers: 5', font=('Arial', 9))
travel_class = canvas.create_text(410, 170, text='Travel Class: Economy', font=('Arial', 9))


airports_ret = canvas.create_text(250, 250, text='Lon - Par', font=('Arial', 15))
logo2 = canvas.create_image(60, 295, image=logo_1)
return_times = canvas.create_text(250, 295, text=f'20:00 - 21:50',fill='black', font=('Arial', 20,))
return_airline = canvas.create_text(420, 295, text='Airline: BA')
price_text = canvas.create_text(250, 380, text=f'£598', fill='red', font=('Arial', 20))


canvas.grid(column=0, row=1, pady=10, padx=10)








window.mainloop()















