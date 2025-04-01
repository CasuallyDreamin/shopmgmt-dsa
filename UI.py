from deli_mgmt import deli_mgmt
from clear_screen import clear

del_mgmt = deli_mgmt()

with open('delivered_parcel.txt','r') as f:
    raw = f.read().split('\n')
    raw.pop()
    data = [line.split(',') for line in raw]
    for parcel in data:
        del_mgmt.ship_mgmt.add_shipment(
            parcel[0],
            parcel[1],
            parcel[2],
            parcel[3],
            parcel[4],
            int(parcel[5]),
            parcel[6]
        )

def UI():
    running = True
    while running:
        clear()
        #show options
        print('''
1. Manage shipments
2. Manage Delivery
3. Best couriers
Z. exit
''')
        opt = input('$')
        
        #apply logic
        if opt == 'Z':
            running = False
            clear()

        elif opt == '1':
            #show shipment management options
            clear()
            aopt = input('''
1. Add Shipment
2. Find Shipment by ID
3. Find Shipments by Price range
4. Show All Shipments
''')
            valid_options = ['1','2','3','4']
            if aopt not in valid_options:
                input("Invalid Input")
            else:
                handle_shipment_options(aopt)

        elif opt == '2':
            #show delivery management options
            clear()
            aopt = input('''
1. Add courier
2. Find Shipments by courior name
3. Find top k highest delivery couriers
4. Show All couriers
5. Show All shipemnts
6. Show All shipments in queue
7. Show All shipments by date
8. Show All Delivered
9. Show All Failed
10. Assign Shipment to courier
11. Edit courier info
                                                                                                                                                    
''')
            valid_options = ['1','2','3','4','5','6','7','8','9','10','11']
            if aopt not in valid_options:
                input("Invalid Input")
            else:
                handle_deli_options(aopt)

        elif opt == '3':
            #show top couriers
            top_couriers = del_mgmt.get_top_couriers()
            for i in range(top_couriers.size):
                print(top_couriers.get(i).full_name)
        else:
            input("Invalid input")
    
def handle_shipment_options(opt):
    clear()
    if opt == '1':
        ship_id = input("ID:")
        weight = input("weight:")
        sub_id = input("subscription_ID:")
        conf_date = input("Order date(yyyy/mm/dd):")
        delivered_date = input("Delivery date(yyyy/mm/dd):")
        try:
            price = int(input("price:"))
        except:
            input("Invalid price value. must be an integer.")
            return
        
        category = input("Categpry(F:food C:Cleaners O:Other):")

        if del_mgmt.ship_mgmt.add_shipment(
            ship_id,
                weight,
                sub_id,
                conf_date,
                delivered_date,
                price,
                category
        ): input("Done!")
        
        else: input("Invalid Shipment ID or Date format")
    
    elif opt == '2':
        id = input("ID:")
        shipment = del_mgmt.ship_mgmt.get_shipment_by_id(id)
        if shipment != None:
            input(f"{shipment.ship_id},{shipment.weight},{shipment.sub_id},{shipment.conf_date},{shipment.delivered_date},{shipment.price},{shipment.category}")
        else:
            input("Item not found.")

    elif opt == '3':
        limit = input("Max Price:")
        shipments = del_mgmt.ship_mgmt.get_all_by_max_price(limit)
        if not shipments:
            input("No items found or invalid price value")
        else:
            for i in range(shipments.size):
                shipment = shipments.get(i)
                print(f"{shipment.ship_id},{shipment.weight},{shipment.sub_id},{shipment.conf_date},{shipment.delivered_date},{shipment.price},{shipment.category}")
            input("")

    elif opt == '4':
        shipments = del_mgmt.ship_mgmt.get_all_shipments()
        for i in range(shipments.size):
            shipment = shipments.get(i)
            print(f"{shipment.ship_id},{shipment.weight},{shipment.sub_id},{shipment.conf_date},{shipment.delivered_date},{shipment.price},{shipment.category}")
        input("")

    
def handle_deli_options(opt):
    if opt == '1':pass
    elif opt == '2':pass
    elif opt == '3':pass
    elif opt == '4':pass
    elif opt == '5':pass
    elif opt == '6':pass
    elif opt == '7':pass
    elif opt == '8':pass
    elif opt == '9':pass
    elif opt == '10':pass
    elif opt == '11':pass
        



if __name__ == "__main__":
    UI()