# -*- coding: utf-8 -*-





class Box_Handler():
    def __init__(self):
        self.args = ['title','sender','receiver','status']
        self.boxes = {
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
