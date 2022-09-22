import webbrowser

class FlightDetails:

    def __init__(self, flight):
        """The flight details are stored as class attributes, and instances of this class are stored in a list of
        objects, which can be later accessed/referenced"""
        self.departure_airport = flight['flyFrom']
        self.destination_airport = flight['flyTo']
        self.price = flight['price']
        from_date = ((flight['route'][0]['local_departure']).split('T')[0]).split('-')
        to_date = ((flight['route'][1]['local_departure']).split('T')[0]).split('-')
        self.from_date = f'{from_date[2]}/{from_date[1]}/{from_date[0]}'
        self.to_date = f'{to_date[2]}/{to_date[1]}/{to_date[0]}'

        self.depart_time = ((flight['route'][0]['local_departure']).split('T')[1].split('.')[0]).split(':')
        self.arrive_time = ((flight['route'][0]['local_arrival']).split('T')[1].split('.')[0]).split(':')
        self.departure_airline = flight['route'][0]['airline']
        self.depart_time_ret = ((flight['route'][1]['local_departure']).split('T')[1].split('.')[0]).split(':')
        self.arrive_time_ret = ((flight['route'][1]['local_arrival']).split('T')[1].split('.')[0]).split(':')
        self.return_airline = flight['route'][1]['airline']
        self.airline_code_1 = flight['route'][0]['airline']
        self.airline_code_2 = flight['route'][1]['airline']

        travel_class_1 = flight['route'][0]['fare_category']
        travel_class_2 = flight['route'][1]['fare_category']
        self.travel_class_1 = self.convert_class(travel_class_1)
        self.travel_class_2 = self.convert_class(travel_class_2)
        self.payment_url = flight['deep_link']

    def convert_class(self, travel_class):
        """Converts into human-readable form"""
        if travel_class == 'M':
            return 'Economy'
        elif travel_class == 'C':
            return 'Business'
        elif travel_class == 'F':
            return 'First Class'

