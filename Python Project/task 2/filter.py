def check_time(num):
    '''Check if time entered is correct'''
    try:
        num = int(num)
        
        if num >= 0 and num <= 1440: #1440 is the maximum minutes in a day
            return 1
        
        else:
            return 0
        
    except:
        return 0
    

def clean(file):
    '''Filter garbage values'''
    
    with open(file, "r") as source:
        lines = source.readlines()
        
    clean_list = []
    garbage_list = []
    
    for i in lines:
        elements = len(i.split(","))
        
        if elements == 3: #Check if only 3 elements are comma separated
            data = i.strip().split(",")
            owns = data[0].strip().upper()
            
            if owns == "OURS" or owns == "THEIRS":
                enter = data[1].strip()
                exits = data[2].strip()
                
                entry_right = check_time(enter)
                exit_right = check_time(exits)
                
                if entry_right and exit_right:
                    enter = int(enter)
                    exits = int(exits)
                    
                    if exits - enter > 0:
                        clean_list.append(f"{owns},{enter},{exits}")
                    
                    #Every single else statements below to add garbage values to a list
                    else:
                        garbage_list.append(i)

                else: 
                    garbage_list.append(i)
            
            else:
                garbage_list.append(i)
                
        else:
            garbage_list.append(i)
            
    return clean_list, garbage_list
