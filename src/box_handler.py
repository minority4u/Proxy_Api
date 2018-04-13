# -*- coding: utf-8 -*-





class Box_Handler():
    def __init__(self):
        self.args = ['title','sender','receiver','status']
        self.args = ['current_adress',
                    'destination_adress',
                    'status',
                    'size',
                    'weight']
        self.boxes =    {
                10100 : {
             
            'current_FirstName' : 'Bernd',
            'current_LastName': 'Mustermann',
            'current_Street' : 'ExampleStreet',
            'current_StreetNo': '123',
            'current_Plz': '68167',
            'current_City' : 'Mannheim',
            'current_Country' : 'Germany',
            'current_StartDate' : '2018-04-23T18:25:43',
            'current_EndDate' : '2018-05-23T18:25:43.511Z',
            'destination_FirstName' : 'Bernd',
            'destination_LastName': 'Mustermann',
            'destination_Street' : 'ExampleStreet',
            'destination_StreetNo': '123',
            'destination_Plz': '68167',
            'destination_City' : 'Mannheim',
            'destination_Country' : 'Germany',
            'destination_StartDate' : '2018-04-23T18:25:43',
            'destination_EndDate' : '2018-05-23T18:25:43.511Z',
            'status' : 'readyToShip',
            'size' : 'M',
            'weight' : '2kg'
            },
                    10101 : {            'current_FirstName' : 'Bernd',
            'current_LastName': 'Mustermann',
            'current_Street' : 'ExampleStreet',
            'current_StreetNo': '123',
            'current_Plz': '68167',
            'current_City' : 'Mannheim',
            'current_Country' : 'Germany',
            'current_StartDate' : '2018-04-23T18:25:43',
            'current_EndDate' : '2018-05-23T18:25:43.511Z',
            'destination_FirstName' : 'Bernd',
            'destination_LastName': 'Mustermann',
            'destination_Street' : 'ExampleStreet',
            'destination_StreetNo': '123',
            'destination_Plz': '68167',
            'destination_City' : 'Mannheim',
            'destination_Country' : 'Germany',
            'destination_StartDate' : '2018-04-23T18:25:43',
            'destination_EndDate' : '2018-05-23T18:25:43.511Z',
            'status' : 'readyToShip',
            'size' : 'M',
            'weight' : '2kg'
      },
                    10102 : {            'current_FirstName' : 'Bernd2',
            'current_LastName': 'Mustermann',
            'current_Street' : 'ExampleStreet',
            'current_StreetNo': '123',
            'current_Plz': '68167',
            'current_City' : 'Mannheim',
            'current_Country' : 'Germany',
            'current_StartDate' : '2018-04-23T18:25:43',
            'current_EndDate' : '2018-05-23T18:25:43.511Z',
            'destination_FirstName' : 'Bernd',
            'destination_LastName': 'Mustermann',
            'destination_Street' : 'ExampleStreet',
            'destination_StreetNo': '123',
            'destination_Plz': '68167',
            'destination_City' : 'Mannheim',
            'destination_Country' : 'Germany',
            'destination_StartDate' : '2018-04-23T18:25:43',
            'destination_EndDate' : '2018-05-23T18:25:43.511Z',
            'status' : 'readyToShip',
            'size' : 'M',
            'weight' : '2kg'
      },
                    10103 : {            'current_FirstName' : 'Bernd3',
            'current_LastName': 'Mustermann',
            'current_Street' : 'ExampleStreet',
            'current_StreetNo': '123',
            'current_Plz': '68167',
            'current_City' : 'Mannheim',
            'current_Country' : 'Germany',
            'current_StartDate' : '2018-04-23T18:25:43',
            'current_EndDate' : '2018-05-23T18:25:43.511Z',
            'destination_FirstName' : 'Bernd',
            'destination_LastName': 'Mustermann',
            'destination_Street' : 'ExampleStreet',
            'destination_StreetNo': '123',
            'destination_Plz': '68167',
            'destination_City' : 'Mannheim',
            'destination_Country' : 'Germany',
            'destination_StartDate' : '2018-04-23T18:25:43',
            'destination_EndDate' : '2018-05-23T18:25:43.511Z',
            'status' : 'readyToShip',
            'size' : 'M',
            'weight' : '2kg'
      },
                    10104 : {            'current_FirstName' : 'Bernd4',
            'current_LastName': 'Mustermann',
            'current_Street' : 'ExampleStreet',
            'current_StreetNo': '123',
            'current_Plz': '68167',
            'current_City' : 'Mannheim',
            'current_Country' : 'Germany',
            'current_StartDate' : '2018-04-23T18:25:43',
            'current_EndDate' : '2018-05-23T18:25:43.511Z',
            'destination_FirstName' : 'Bernd',
            'destination_LastName': 'Mustermann',
            'destination_Street' : 'ExampleStreet',
            'destination_StreetNo': '123',
            'destination_Plz': '68167',
            'destination_City' : 'Mannheim',
            'destination_Country' : 'Germany',
            'destination_StartDate' : '2018-04-23T18:25:43',
            'destination_EndDate' : '2018-05-23T18:25:43.511Z',
            'status' : 'readyToShip',
            'size' : 'M',
            'weight' : '2kg'
      }
     }
        self.boxes_old = {
    1 : {
        'title': u'Reusable Box - original shipment',
        'sender': 'Max Mueller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status:' : 'sold'
    },
    2 : {
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Mueller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
        },
    3 : {
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Mueller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
    },
    4 : {
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Mueller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
    },
    5 : {
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Mueller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
    }
}






    def get_boxes(self):
        return self.boxes

    def get_args(self):
        return self.args

if __name__ == '__main__':
    print(Box_Handler().get_boxes())
