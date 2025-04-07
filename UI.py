from deli_mgmt import deli_mgmt
from clear_screen import clear
from datetime import datetime

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

        ship_id = input("ID (ABC1234):")
        num_c = 0
        alpha_c = 0
        for char in ship_id:
            if char.isalpha():alpha_c += 1
            if char.isnumeric():num_c += 1
        if num_c + alpha_c != 7 or len(ship_id) != 7: return input("ID must be 7 digits long.")
        if num_c != 4: return input("ID must have 4 numbers.")
        if alpha_c != 3: return input("ID must have 3 alphabets.")
            
        try: weight = int(input("weight:"))
        except: return input("Weight must be a number.")   
        if weight < 0: return input("Weight cannot be negative.")
        
        sub_id = input("subscription_ID:")
        if len(sub_id) != 8: return input("Must have 8 digits.")
        try: sub_id = int(sub_id)
        except: input("subscription ID must be a number.")

        try: price = int(input("price:"))        
        except: return input("Invalid price value. must be an integer.")
        if price < 0: return input("Price cannot be a negative.")
        
        conf_date = input("Order date(year-month-day):").split('-')
        try: conf_date = datetime(int(conf_date[0]), int(conf_date[1]), int(conf_date[2])).date()
        except: return input("Invalid date format.")
            
        delivered_date = input("Delivery date(year-month-day):").split('-')
        try: delivered_date = datetime(int(delivered_date[0]), int(delivered_date[1]), int(delivered_date[2])).date()
        except: return input("invalid date format.")    
        if delivered_date < conf_date: return input("Delivered date cannot be before Order date.")

        category = input("Categpry(F:food C:Cleaners O:Other):")
        if category not in ['F', 'C', 'O']: return input("invalid category.")
            
        if del_mgmt.ship_mgmt.add_shipment(
            ship_id,
                weight,
                sub_id,
                conf_date,
                delivered_date,
                price,
                category
        ): 
            input("Done!")
            
            file_shipment_format = '\n'\
            + ship_id + ','\
            + str(weight) + ','\
            + str(sub_id) + ','\
            + str(conf_date) + ','\
            + str(delivered_date) + ','\
            + str(price) + ','\
            + category
    
            with open('delivered_parcel.txt','a') as f:
                f.write(file_shipment_format)

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