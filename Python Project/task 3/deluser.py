def del_user(pw):
    
    import codecs
    import getpass
    
    username = input("\nEnter username: ")
    password = getpass.getpass("\nEnter password: ")
    password = codecs.encode(password, "rot_13")
    
    with open(pw, "rt") as file:
        lines = file.readlines()
    
    delete = False
    
    with open(pw, "w") as file:
        
        for i in lines:
            new_line = i.strip().split(":")
            
            if new_line[0] == username and new_line[2] == password:
                delete = True
                
            else:
                file.write(i)
        
    if delete:
        print("\nUser deleted!")
    
    else:
        print("\nUser not found or wrong password!")
      