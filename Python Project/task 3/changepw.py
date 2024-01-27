def changepw_user(pw):
    import codecs
    import getpass
    
    with open(pw, "rt") as file:
        lines = file.readlines()
    
    username = input("\nEnter username: ")
    password = getpass.getpass("\nEnter password: ")
    password = codecs.encode(password, "rot_13")
    
    with open(pw, "w") as new:
        
        found = False
        
        for i in lines:
            
            data = i.strip().split(":")
            
            un = data[0]
            rn = data[1]
            pw = data[2]
            
            if username == un:
                
                found = True
                
                if pw == password:
                    new_pw = getpass.getpass("\nEnter new password: ")
                    new_pw = codecs.encode(new_pw, "rot_13")
                
                    if new_pw != password:
                        conf_pw = getpass.getpass("\nConfirm password: ")
                        conf_pw = codecs.encode(conf_pw, "rot_13")
                        
                        if new_pw == conf_pw:
                            new.write(f"{un}:{rn}:{conf_pw}\n")
                            print("\nChanged Password!")
                            
                        else:
                            print("\nPassword cannot be same as before!")
                            new.write(i)
                            
                    else:
                        print("\nWrong Password!")
                        new.write(i)

                else:
                    print("\nPassword does not match")
                    new.write(i)
                
            else:
                new.write(i)
                
        if found == False:
            print("\nUser not found!\n")
