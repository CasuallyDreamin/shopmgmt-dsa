from dll import dll

class courier:
    def __init__(self,
    employment_id,
    national_id,
    name,
    family_name,
    capacity = 1,
    availability = 'A'):
        self.employment_id = employment_id
        self.national_id = national_id
        self.name = name
        self.family_name = family_name
        self.full_name = name + ' ' + family_name
        self.capacity = capacity
        self.is_available = availability
        self.shipment_history = dll()
        self.delivered = 0

    def assign_shipment(self, shipment):
        self.shipment_history.add_last(shipment)
        self.delivered += 1

    def get_data(self):
        data = [self.name, self.family_name, self.national_id, str(self.capacity), self.is_available]
        return data
        