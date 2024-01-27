import task1input as t1
import time
import os
    
sno = 1 #serial number of the user

try:
    with open("pizzarecords.csv", "r") as file:
        lines = file.readlines()
        line = lines[-1]
        serial = line.strip().split(",")[0]
        
        if serial != "SNO":
            sno = int(serial) + 1 #Sets the serial number 1 more than the one stored in the file

except FileNotFoundError:
    print("\nCouldn't read file as file doesn't exist.")
    time.sleep(2)

user_list = [] #To write in the file

while True:
    
    def pizza_count(pizza_type, pizza_price):
        '''Calculates price for total pizzas'''

        added_price = 0
        
        for key in pizza_type:
            if key in pizza_price.keys():
                new_price = pizza_type[key] * float(pizza_price[key][1:])
                added_price += new_price

        return added_price

    def day_check(price, day = "no"):
        '''Checking if it's Tuesday for discount'''
            
        if day == "y" or day == "yes":
            price = price - (50/100) * price
            
        elif day == "n" or day =="no":
            pass

        else:
            print("y or n only")
        
        return price

    def app_check(price, app_order = "n"):
        '''Check if ordered by app for discount'''
        
        if app_order == "y" or app_order == "yes":
            price  = price - (25/100) * price

        elif app_order == "n" or app_order == "no":
            pass

        else:
            print("y or n only")
            
        return price
        
    def delivery_check(price, delivery, pizza_no):
        '''Check if delivery is required or not, add price for small orders'''
        
        if delivery == "y" or delivery == "yes":
            if pizza_no < 5:
                price = price + 2.5

        elif delivery == "n" or delivery == "no":
            pass

        else:
            print("y or n only")
        
        return price

    def output(day_discount, app_discount, delivery_fee, delivery_price, new_price, pizza_type, pizza_price):
        '''Final output formatting'''
        
        delivery_fee_1 = delivery_fee
        day_discount = f'-£{day_discount:.2f}'
        app_discount = f'-£{app_discount:.2f}'
        delivery_fee = f'+£{delivery_fee:.2f}'
        delivery_fee_1 = f'£{delivery_fee_1:.2f}'
        delivery_price = f'£{delivery_price:.2f}'
        
        p1 = 'Amount'
        p2 = 'Tuesday Discount'
        p3 = 'App Discount'
        p4 = 'Delivery Fee'
        p5 = 'Total Price'
            
        os.system('cls')
        print("\tBECKETT PIZZA PLAZA")
        print()
        print("="*45)
        print(f"Orders {'Count':>24} {'Price':>11}\n")

        count = 1
        individual = []
        
        for key in pizza_type:
            if key in pizza_price.keys():
                val = pizza_type[key] * float(pizza_price[key][1:]) #Get the price of a specific pizza
                val = f"£{val}0"
                individual.append(val)
        
        new_price = f'£{new_price:.2f}'
                
        for i, j in pizza_type.items():
            #Formatting the alignment of the displayed bill
            print(f"{count}. {i} {j:>{25 - len(i)}} {individual[count-1]:>{14-len(str(j)) if len(str(j)) == 1 else 15-(len(str(j)))}}")
            count += 1

        print()
        print("=" * 45)
        print(f"{p1} {new_price:>{42 - len(p1)}}")
        print(f"{p2} {day_discount:>{42 - len(p2)}}")
        print(f"{p3} {app_discount:>{42 - len(p3)}}")
        if delivery_fee == '+£0.00':
            print(f"{p4} {delivery_fee_1:>{42 - len(p4)}}")
        else:
            print(f"{p4} {delivery_fee:>{42 - len(p4)}}")
        print()
        print("=" * 45)
        print(f"{p5} {delivery_price:>{42 - len(p5)}}")
        print()
        print("=" * 45)
        print("THANK YOU FOR YOUR VISIT!")    
        
        time.sleep(3)
        
    os.system('cls')

    price = 12

    pizza_no, delivery, day, app_order, pizza_type, pizza_price = t1.user_input()

    if not day:
        if time.localtime()[6] == 1: #Index 6 of local time contains the value for day. (Mon to Sunday, 0 to 6, 1 = Tuesday)
            day = "yes"
        else:
            day = "no"
        
    new_price = pizza_count(pizza_type, pizza_price)
    day_price = day_check(new_price, day)
    app_price = app_check(day_price, app_order)
    delivery_price = delivery_check(app_price, delivery, pizza_no)

    day_discount = new_price - day_price
    app_discount = day_price - app_price
    delivery_fee = delivery_price - app_price

    output(day_discount, app_discount, delivery_fee, delivery_price, new_price, pizza_type, pizza_price)
    
    user_list.append((sno, delivery_price, pizza_no, delivery, day, app_order))
    sno += 1 #Increasing serial number for next user
    
    temp_list = []
    
    for i in user_list:
        temp_list.append(f"{i[0]},{i[1]},{i[2]},{i[3]},{i[4]},{i[5]}\n")
    
    try:
        with open("pizzarecords.csv", "a") as file:
            file.write(temp_list[-1])
            
    except FileNotFoundError:
        print("\nCouldn't write to file as file doesn't exist.")
    
    while True:
        cont = input("\nContinue? ")
        cont = cont.strip().lower()
        
        if cont == "y" or cont == "yes" or cont == "n" or cont == "no":
            break
        
        elif cont == '':
            cont = "n"
            break
        
        else:
            print("\nPlease enter yes or no only (y/n)\n")
            
    if cont == 'n' or cont == 'no':
        os.system('cls')
        
        print("Session log:")
        print("\nuser:total:orders:delivery:day:app")
        
        for i in user_list:
            print(f"\n{i[0]}:{i[1]}:{i[2]}:{i[3]}:{i[4]}:{i[5]}")
            
        print()
        
        break
