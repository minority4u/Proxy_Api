# -*- coding: utf-8 -*-

class BoxModel:
    def __init__(self, current_adress_args, destination_adress_args, status, size, weight):
        # We will automatically generate the new id
        self.id = 0
        self.current_adress = AdressModel(current_adress_args)
        self.destination_adress = AdressModel(destination_adress_args)
        self.status = status
        self.size = size
        self.weight = weight

class AdressModel:
    def __init__(self, first_name, last_name, street, street_no, plz, city, country, start_date, end_date):
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.street_no = street_no
        self.plz = plz
        self.city = city
        self.country = country
        self.start_date = start_date
        self.end_date = end_date
        
        
if __name__ == '__main__':
    import os
    print(os.path.splitext("path_to_file")[0])