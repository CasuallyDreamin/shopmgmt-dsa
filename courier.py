from dll import dll

class courier:
    def __init__(self,
    employment_id,
    national_id,
    name,
    family_name,
    capacity = 1):
        self.employment_id = employment_id
        self.national_id = national_id
        self.name = name
        self.family_name = family_name
        self.full_name = name + ' ' + family_name
        self.capacity = capacity
        self.is_available = True
        self.shipment_history = dll()
        self.delivered = 0
    
        