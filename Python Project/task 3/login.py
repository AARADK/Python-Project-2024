def login_user(pw):
    
    import codecs
    import getpass
    
    with open(pw, "rt") as file:
        lines = file.readlines()
    
    while True:
        username = input("\nEnter username: ")
        if username:
            break
    
    while True:    
        password = getpass.getpass("\nEnter password: ")
        if password:
            break
        
    password = codecs.encode(password, "rot_13")
    
    found = False
    
    for i in lines:
        new_line = i.strip().split(":")
        if username == new_line[0] and password == new_line[2]:
            print("\nLogin Successful")
            found = True
    
    if found == False:
        print("\nUser not found or wrong password!")
