class shipment:
    def __init__(self,
                 ship_id,
                 weight,
                 sub_id,
                 conf_date,
                 delivered_date,
                 price,
                 category):
                
        self.ship_id = ship_id
        self.weight = weight
        self.sub_id = sub_id
        self.conf_date = conf_date
        self.delivered_date = delivered_date
        self.price = price
        self.category = category