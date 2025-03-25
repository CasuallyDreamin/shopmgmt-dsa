from dll import dll
from hashtable import hashtable
from shipment import shipment
from tools import generate_ship_id
from arr import arr

class mgmt:
    def __init__(self):
        #hashtable for O(1) average-case and O(n) worst-case look up
        #doubly linked list for O(n) show all items
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
        
        #generating unique shipment id if none given
        while ship_id == None or self.shipments_ht.get(ship_id) != None:
            ship_id = generate_ship_id(category)

        new_shipment = shipment(ship_id,
                 weight,
                 sub_id,
                 conf_date,
                 arrival_date,
                 price,
                 category)
        
        self.shipments_ht.insert(new_shipment.ship_id, new_shipment)

    def get_shipment_by_id(self, shipment_id) -> shipment | None:
        return self.shipments_ht.get(shipment_id)
    
    def get_all_shipments(self) -> arr:
        return self.shipments_dll.get_all_arr()
    
    def get_all_by_max_price(self, max_price) -> arr | None:
        curr_shipment = self.shipments_dll.head
        target_shipments = dll()

        if curr_shipment == None:
            return None
        
        while curr_shipment != None:
            if curr_shipment.data.price <= max_price:
                target_shipments.add_first(curr_shipment.data)
            curr_shipment = curr_shipment.next

        return target_shipments.get_all_arr()

        


    
        
