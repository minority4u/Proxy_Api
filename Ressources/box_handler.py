# -*- coding: utf-8 -*-





class Box_Handler():
    def __init__(self):
        self.boxes = {
    1 : {
        'id': 1,
        'title': u'Reusable Box - original shipment',
        'sender': 'Max Müller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status:' : 'sold' 
    },
    2 : {
        'id': 2,
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Müller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
        
    },
            3 : {
        'id': 3,
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Müller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
        
    },
                    4 : {
        'id': 4,
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Müller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
        
    },
                            5 : {
        'id': 5,
        'title': u'Reusable Box - cross-docking',
        'sender': 'Max Müller, Lange strasse 2, 68167 Mannheim',
        'receiver': 'Lise Mustermann, kurzes Eck, 99999 Muenchen',
        'status' : 'returned'
        
    }
}
    def get_boxes(self):
        return self.boxes
    
def __main__():
    pass
