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
with open('delivery_information.txt','r') as f:
    raw = f.read().split('\n')
    raw.pop()
    data = [line.split(',') for line in raw]
    for parcel in data:
        del_mgmt.add_courier(
            parcel[2],
            parcel[0],
            parcel[1],
            int(parcel[3]),
            parcel[4]
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
5. Show All deliveries
6. Show All deliveries in queue
7. Show All deliveries by date
8. Show All Delivered shipments
9. Show All Failed shipments
10. Assign Delivery to courier
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
    clear()
    if opt == '1':
        try: national_id = int(input("National ID:"))
        except: return input('national ID must be an integer.')
        
        #todo: check unique national ID

        name = input("Name:")
        family_name = input("Family Name:")
        
        try: 
            capacity = int(input("capacity:"))
            if capacity < 1: return input("capacity cannot be less than 1.")
        except: return input("capacity must be an integer.")
        
        availability = input("availability(A:Available / D:Not Available, case sensitive):")
        if availability not in ['A','D']: return input('invalid new availability.')
         
        del_mgmt.add_courier(national_id, name, family_name, capacity, availability)
        courier_format = '\n'\
        + name + ','\
        + family_name + ','\
        + str(national_id) + ','\
        + str(capacity) + ','\
        + availability
    
        with open('delivery_information.txt','a') as f:
            f.write(courier_format)

        return input('Done!')
                    
    elif opt == '2':
        name = input("Name:")
        family_name = input("Family Name:")
         
        shipments = del_mgmt.get_all_shipments_by_courier_full_name(name + ' ' + family_name)
        if shipments:
            for i in range(shipments.size):
                temp = shipments.get(i)
                print(temp.ship_id)
            
            return input()
        
        else: return input("Courier not found.")
        
    elif opt == '3':
        try: top_couriers = del_mgmt.get_top_couriers(int(input("Enter number of top couriers:")))
        except: input("Must enter a positive integer.")
        
        print("id, full name, delivery count")
        for i in range(top_couriers.size):
            temp = top_couriers.get(i)
            print(f"{temp.employment_id},{temp.full_name},{temp.delivered}")
        
        return input()
    
    elif opt == '4':
        couriers = del_mgmt.get_all_couriers()
        print("Employment ID , National ID , Full name , Capacity , Availability")
        for i in range(couriers.size):
            temp = couriers.get(i)
            print(f"{temp.employment_id},{temp.national_id},{temp.full_name},{temp.capacity},{temp.is_available}")
        
        return input()

    elif opt == '5':
        deliveries = del_mgmt.get_all_deliveries()
        for i in range(deliveries.size):
            temp = deliveries.get(i)
            print(temp.courier,",",temp.shipment)
        return input()
    
    elif opt == '6':
        deliveries = del_mgmt.get_all_deliveries_in_queue()
        for i in range(deliveries.size):
            temp = deliveries.get(i)
            print(temp.courier,",",temp.shipment)
        return input()
    
    elif opt == '7':
        date = input("Enter Date(year-month-day):").split('-')
        
        try: date = datetime(int(date[0]), int(date[1]), int(date[2])).date()
        except: return input("invalid date format.")    

        deliveries = del_mgmt.get_deliveries_by_date(date)

        for i in range(deliveries.size):
            temp = deliveries.get(i)
            print(temp.courier,",",temp.shipment)

        return input()

    elif opt == '8':
        deliveries = del_mgmt.get_all_delivered()
        
        for i in range(deliveries.size):
            temp = deliveries.get(i)
            print(temp.courier,",",temp.shipment)
        return input()
    
    elif opt == '9':
        deliveries = del_mgmt.get_all_failed()
        
        for i in range(deliveries.size):
            temp = deliveries.get(i)
            print(temp.courier,",",temp.shipment)
        return input()
    
    elif opt == '10':
        try: 
            courier_id = int(input('Enter courier ID:'))
            if courier_id < 0:
                return input("Must be a positive number.")
        except: return input("Must Enter an integer.")

        ship_id = input("Enter shipment ID:")
        if not del_mgmt.assign_shipment(ship_id, courier_id): return input("courier not found/isn't available or shipment not found.")
        else: return input("Done!")

    elif opt == '11':
        try:
            courier_id = int(input("Enter employment ID:"))
            if courier_id < 1: return input("Employment ID must be positive.")
            if not del_mgmt.couriers_ht.get(courier_id): return input("courier not found.")
        except: return input("Employment ID must be an integer.")
        courier = del_mgmt.couriers_ht.get(courier_id)
        print(f'''National ID:{courier.national_id}
Name:{courier.name}
Family Name:{courier.family_name}
Capacity:{courier.capacity}
Availability:{courier.is_available}
''')
        print("leave blank to keep old data.")
        
        new_national_id = input("new national ID:")
        new_name = input("new name:")
        new_family_name = input("new family name:")
        new_capacity = (input("new capacity:"))

        if new_capacity != '':
            try: 
                new_capacity = int(new_capacity)
                if new_capacity < 1: return input("new capacity cannot be less than 1.")
            except: return input("new capacity must be an integer.")
       
        new_availability = input("new availability(A:Available / D:Not Available, case sensitive):")
        if new_availability not in ['A','D','']: return input('invalid new availability.')
        
        del_mgmt.edit_courier_data(courier_id, new_national_id, new_name, new_family_name, new_availability, new_capacity)
            
        with open('delivery_information.txt','w') as f:
            all_couriers = del_mgmt.get_all_couriers().array
            all_couriers = [','.join(courier.get_data()) for courier in all_couriers]
            f.write('\n'.join(all_couriers))

        return input("Done!")
        



if __name__ == "__main__":
    UI()