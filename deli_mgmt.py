from hashtable import hashtable as ht
from qu import queue as Q
from dll import dll
from courier import courier
from arr import arr
from ship_mgmt import ship_mgmt
from delivered import delivered
from failed_delivery import failed_delivery
from delivery import delivery
from datetime import datetime
class deli_mgmt:
    def __init__(self):
        self.date = datetime.today().date()
        self.employment_id_index = 1
        self.couriers_ht = ht()
        self.couriers_dll = dll()
        self.ship_mgmt = ship_mgmt()
        self.deliveries_ht = ht()
        self.deliveries_dll = dll()
        self.delivery_queue = Q()
        self.delivered = dll()
        self.failed = dll()
    
    def add_courier(self, national_ID, name, family_name, capacity, availability):
        new_courier = courier(self.employment_id_index, national_ID, name, family_name, capacity, availability)
        self.employment_id_index += 1
        self.couriers_dll.add_last(new_courier)
        self.couriers_ht.insert(new_courier.employment_id, new_courier)
        return True
    
    def get_courier_by_full_name(self, full_name) -> courier:
        
        curr_courier = self.couriers_dll.head

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
    
    def get_all_deliveries(self):
        return self.deliveries_dll.get_all_arr()
    
    def get_all_deliveries_in_queue(self):
        return self.delivery_queue.get_all()
    
    def get_deliveries_by_date(self, date):
        delivered = self.delivered.get_all_arr()
        result = dll()

        for i in range(delivered.size):
            temp = delivered.get(i)
            if temp.date == date:
                result.add_first(temp)

        return result.get_all_arr()
    
    def get_all_delivered(self):
        return self.delivered.get_all_arr()
    
    def get_all_failed(self):
        return self.failed.get_all_arr()

    def assign_shipment(self, ship_id, courier_id):
        cour:courier = self.couriers_ht.get(courier_id)

        if cour == None:
            return False

        if cour.is_available != "A":
            return False
        
        if not self.deliveries_ht.get(ship_id):
            return False

        cour.assign_shipment(ship_id)
        self.delivered.add_first(delivered(courier_id, ship_id,self.date))

    def edit_courier_data(self,
            employment_id,
            new_national_id,
            new_name,
            new_family_name,
            new_avail,
            new_capacity):
        
        target_courier:courier = self.couriers_ht.get(employment_id)

        if target_courier == None:
            return False
        
        if new_name != '':
            target_courier.name = new_name
            target_courier.full_name = target_courier.name + ' ' + target_courier.family_name
        
        if new_family_name != '':
            target_courier.family_name = new_family_name
            target_courier.full_name = target_courier.name + ' ' + target_courier.family_name
        

        if new_capacity != '':
            target_courier.capacity = new_capacity

        if new_national_id != '':
            target_courier.national_id = new_national_id
            
        if new_avail != '':
            target_courier.is_available = new_avail

        self.couriers_ht.update(employment_id, target_courier)