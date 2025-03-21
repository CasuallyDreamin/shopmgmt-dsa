from dll import dll
from hashtable import hashtable
from shipment import shipment
from tools import generate_ship_id

class mgmt:
    def __init__(self):
        #placeholder DS (should add array/hashtable for O(n) look up)
        self.shipments_ht = hashtable()
        self.shipments_dll = dll()

    def add_shipment(self,
                ship_id,
                weight,
                sub_id,
                conf_date,
                arrival_date,
                price,
                category):
        
        while ship_id == None or self.shipments_ht.get(ship_id) != None:
            ship_id = generate_ship_id(category)

        new_shipment = shipment(ship_id,
                 weight,
                 sub_id,
                 conf_date,
                 arrival_date,
                 price,
                 category)
        
