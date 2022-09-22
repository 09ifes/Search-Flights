import requests
from results_ui import *
import os


tequila_APIKEY = os.environ.get('API_KEY')
search_endpoint = 'https://tequila-api.kiwi.com/v2/search'
tequila_endpoint = 'https://tequila-api.kiwi.com/locations/query'

class FlightSearch:
    def __init__(self, fly_from, fly_to, date_from, date_to, passengers, travel_class, window):
        """Retrieves all the inputted data and saves them to class attributes that can be referenced later on"""
        self.window = window      # Receives the same window object from flight search to be reused
        self.fly_from = self.get_iata_code(fly_from)
        self.fly_to = self.get_iata_code(fly_to)
        self.date_from = date_from
        self.date_to = date_to
        self.flight_type = "round"
        self.data = 0
        self.passengers = passengers
        self.travel_class = self.convert_class(travel_class)
        self.check_flights()


    def convert_class(self, travel_class):
        """Converts selected class to a single letter to make compatible with the search api"""
        if travel_class == 'Economy':
            return 'M'
        elif travel_class == 'Business':
            return 'C'
        elif travel_class == 'First Class':
            return 'F'

    def get_iata_code(self, place):
        """Converts location to iata code to make compatible with the search api"""
        parameters = {
            'term': place,
        }
        header = {
            'apikey': tequila_APIKEY
        }
        response = requests.get(url=tequila_endpoint, params=parameters, headers=header)
        response.raise_for_status()
        iata_code = response.json()['locations'][0]['code']
        return iata_code


    def check_flights(self):
        """Executes api call using the set parameters, and retrieves the flight data"""
        header = {
            'apikey': tequila_APIKEY
        }

        parameters = {
            'fly_from': self.fly_from,
            'date_from': self.date_from,
            'date_to': self.date_from,
            'return_from': self.date_to,
            'return_to': self.date_to,
            'fly_to': self.fly_to,
            "flight_type": self.flight_type,
            "max_stopovers": 0,
            "curr": "GBP",
            'one_for_city': 0,
            'selected_cabins': self.travel_class,
            'adults': self.passengers,
        }
        response = requests.get(url=search_endpoint, headers=header, params=parameters)

        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print('Error, please check the details entered')
        data = response.json()
        try:
            data['data'][0]
        except IndexError:
            print('There were no flights found')
        else:
            self.search_results(data)            # Executes if no exceptions


    def search_results(self, data):
        """Handles flight data and passes to results ui class, execution continues in results_ui.py"""
        self.data = data
        flights_list = self.data['data']
        result_ui = ResultsUI(self.window, flights_list, self.passengers)
        result_ui.flight_results_ui()


