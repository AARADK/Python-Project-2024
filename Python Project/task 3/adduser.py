def add_user(pw):
    
    import codecs
    import getpass
    
    with open(pw, "rt") as file:
        lines = file.readlines()
    
    while True:
        user_name = input("\nEnter a user name: ")
        if user_name:
            break
    
    while True:    
        name = input("\nEnter your full name: ")
        if name:
            break
        
    name = name.title()
    
    while True:
        password = getpass.getpass("\nEnter password: ")
        if password:
            break
        
    password = codecs.encode(password, "rot_13")

    users = []
    for i in lines:
        usr = i.strip().split(":")[0]
        users.append(usr)

    new_usr = []

    if user_name not in users:
        new_usr = f"{user_name}:{name}:{password}\n"
        
        with open(pw, "a") as new_file:
            new_file.write(new_usr)
            
        print("\nUser created!")
        
    else:
        print("Username already exists, please enter new username!")
        add_user()
    