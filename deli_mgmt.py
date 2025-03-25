from hashtable import hashtable as ht
from qu import queue as Q
from dll import dll
from courier import courier
from arr import arr
from ship_mgmt import ship_mgmt

class deli_mgmt:
    def __init__(self):
        self.employment_id_index = 1
        self.couriers_ht = ht()
        self.couriers_dll = dll()
        self.ship_mgmt = ship_mgmt()
        self.shipment_queue = Q()
        self.sent = dll()
        self.failed = dll()
    
    def add_courier(self, national_ID, full_name):
        new_courier = courier(self.employment_id_index, national_ID)
        self.employment_id_index += 1
        self.couriers_dll.add_first(new_courier)
        self.couriers_ht.insert(new_courier.employment_id, new_courier)
        return True
    
    def get_courier_by_full_name(self, name, family_name) -> courier:
        
        curr_courier = self.couriers_dll.head
        full_name = name + ' ' + family_name

        while curr_courier != None:
            if curr_courier.data.full_name == full_name:
               return curr_courier.data
            
            curr_courier = curr_courier.next

        return None

    def get_all_shipments_by_courier_full_name(self, full_name):
        target_courier = self.get_courier_by_full_name(full_name)
        if target_courier == None:
            return None
        
        return target_courier.shipment_history.get_all_arr()
    
    def get_top_couriers(self, count) -> arr:
        if count >= self.couriers_dll.size:
            return self.couriers_dll.get_all_arr()
        
        curr_courier = self.couriers_dll.head
        target_couriers = arr(count)
        min_in_list = curr_courier.data.delivered
        min_index = 0

        for i in range(count):
            target_couriers.insert(i, curr_courier.data)
            
            if curr_courier.data.delivered < min_in_list:
                min_in_list = curr_courier.data.delivered
                min_index = i

            curr_courier = curr_courier.next

        while curr_courier != None:
            if curr_courier.data.delivered > min_in_list:
                target_couriers.insert(min_index, curr_courier.data)
                min_in_list = curr_courier.data.delivered

                for i in range(count):
                    if target_couriers.get(i).delivered < min_in_list:
                        min_in_list = target_couriers.get(i).delivered
                        min_index = i

            curr_courier = curr_courier.next

        return target_couriers
    
    def get_all_couriers(self):
        return self.couriers_dll.get_all_arr()
    
    def get_all_shipments(self):
        return self.ship_mgmt.get_all_shipments()
    
    def get_all_shipments_in_queue(self):
        return self.shipment_queue.get_all()
    
    #todo: change sent data stracture to access shipments by date (direct access table + dll)
    def get_shipments_by_date(self, date):
        return self.ship_mgmt.get_shipment_by_date(date)
    
    def get_all_shipments_send(self):
        return self.sent.get_all_arr()
    
    def get_all_shipments_failed(self):
        return self.failed.get_all_arr()

    def assign_shipment(self, shipment, delivery):
        #todo: assignment logic
        return

    def edit_courier_data(self,
            employment_id,
            new_national_id = None,
            new_name = None,
            new_family_name = None,
            avail_switch = False,
            new_capacity = None):
        
        target_courier:courier = self.couriers_ht.get(employment_id)

        if target_courier == None:
            return False
        
        if new_name != None:
            target_courier.name = new_name
        
        if new_family_name != None:
            target_courier.family_name = new_family_name

        if new_capacity != None:
            target_courier.capacity = new_capacity

        if new_national_id != None:
            target_courier.national_id = new_national_id
            
        if avail_switch:
            target_courier.is_available = not target_courier.is_available
