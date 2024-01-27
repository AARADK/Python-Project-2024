if __name__ != "__main__": #Only run when imported
    import os
    import time
    import sys
    
    def types():
        '''Create a tuple and dictionary for menu'''
        
        m1 = "Cheese Pizza"
        m2 = "Chicken Pizza"
        m3 = "Pepperoni Pizza"
        m4 = "Margherita Pizza"
        m5 = "Hawaiian Pizza"
        m6 = "New York Style Pizza"
        m7 = "Roman Pizza"
        m8 = "Greek Pizza"
        m9 = "Detroit Pizza"
        pizza_type = (m1, m2, m3, m4, m5, m6, m7, m8, m9)
        
        pizza_price = {
            m1 : "£4",
            m2 : "£6",
            m3 : "£6",
            m4 : "£5",
            m5 : "£5",
            m6 : "£8",
            m7 : "£7",
            m8 : "£6",
            m9 : "£10"
        }
        return pizza_type, pizza_price
    
    def menu():
        '''Displays menu'''
        
        orders, pizza_price = types()
        price = []
        for i in pizza_price.values():
            price.append(i)
            
        print(f'''\t\tMENU
          
    1. {orders[0]} {price[0]:>{25 - len(orders[0])}}
    2. {orders[1]} {price[1]:>{25 - len(orders[1])}}
    3. {orders[2]} {price[2]:>{25 - len(orders[2])}}
    4. {orders[3]} {price[3]:>{25 - len(orders[3])}}
    5. {orders[4]} {price[4]:>{25 - len(orders[4])}}
    6. {orders[5]} {price[5]:>{25 - len(orders[5])}}
    7. {orders[6]} {price[6]:>{25 - len(orders[6])}}
    8. {orders[7]} {price[7]:>{25 - len(orders[7])}}
    9. {orders[8]} {price[8]:>{25 - len(orders[8])}}
        
          ''')
    
    def user_input():
        '''Takes in fully processed user input'''

        c = 0 #Count when order has been placed
        conf_exit = 0 #Confirm exit when nothing is entered, only works after no orders are placed
        pizza_type = {}
        
        while True:
            
            os.system('cls')
            
            try:
                
                while True:
                    os.system('cls')
                    menu()
                    orders, _ = types()
                    pizza_no = int(input("Select a pizza: "))
                    print(f"\n{orders[pizza_no-1]}")
                    
                    if pizza_no in range(1,10):
                        try:
                            num = int(input("\nHow many? "))
                            
                        except TypeError:
                            print("\nEnter positive integers only!")
                            time.sleep(2)
                            continue
                            
                        except ValueError:
                            print("\nEnter something!")
                            time.sleep(2)
                            continue
                            
                        if num > 0 and num <= 50:
                            #add input orders to a key in pizza_type dictionary, creates order if no values found
                            pizza_type[orders[pizza_no-1]] = pizza_type.get(orders[pizza_no-1], 0) + num
                            c += 1
                            
                        elif num < 0:
                            print("\nCannot be negative!")
                            time.sleep(2)
                            continue
                        
                        elif num > 50:
                            print("\nToo many orders (max 50)")
                            time.sleep(2)
                            continue
                    
                        print("\nEnter without any orders to exit")
                        time.sleep(2)
                        
                    else:
                        os.system('cls')
                        continue
                    
                    os.system('cls')
                    
            except TypeError:
                print("\nPositive integers only\n")
                time.sleep(2)
                os.system('cls')
                
            except ValueError:
                if not conf_exit:
                    if c == 0:
                        print("\nPlease Take An Order :(")
                        conf_exit = 1
                        time.sleep(2)
                        os.system('cls')
                        continue
                    
                    os.system('cls')
                    break
                
                else:
                    sys.exit()
                       
            except KeyboardInterrupt:
                sys.exit()
                
        count = 0
        
        for i in pizza_type.values():
            count += i
        
        os.system('cls')
        
        try:
            while True:
                delivery = input("\nIs delivery required? ")
                delivery = delivery.strip().lower()
                
                if delivery == "y" or delivery == "yes" or delivery == "n" or delivery == "no":
                    break
                
                elif delivery == '':
                    delivery = "n"
                    break
                
                else:
                    print("\nPlease enter yes or no only (y/n)\n")
            
            while True:
                day = input("\nIs it Tuesday? ")
                day = day.strip().lower()
                
                if day == "y" or day == "yes" or day == "n" or day == "no":
                    break
                
                elif day == '':
                    break
                
                else:
                    print("\nPlease enter yes or no only (y/n)\n")
            
            while True:
                app_order = input("\nDid the customer use the app? ")
                app_order = app_order.strip().lower()
                
                if app_order == "y" or app_order == "yes" or app_order == "n" or app_order == "no":
                    break
                
                elif app_order == '':
                    app_order = "n"
                    break
                
                else:
                    print("\nPlease enter yes or no only (y/n)\n")
                    
        except KeyboardInterrupt:
            sys.exit()
                
        os.system('cls')
        
        _, pizza_price = types()
        
        return count, delivery, day, app_order, pizza_type, pizza_price
