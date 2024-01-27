import init
import os

def main():
    '''Main script for the design aspect'''
    
    try:
        import sys
        import adduser, deluser, login, changepw
        
        #Then the sys.argv takes in the resetted passwd.txt file and performs commands given by user
        pw_file = sys.argv[1]

        while True:
            choice = None
            
            #Enter command here
            choice  = input("\npython-cmd: ").strip()

            if choice == 'adduser':
                adduser.add_user(pw_file)
                
            elif choice == 'login':
                login.login_user(pw_file)
                
            elif choice == 'passwd':
                changepw.changepw_user(pw_file)
                
            elif choice == 'deluser':
                deluser.del_user(pw_file)
                
            elif choice == 'cls' or choice == 'clear':
                os.system('cls')
            
            elif choice == 'help':
                print("\nadduser     Creates a new user")
                print("login       Check for login")
                print("passwd      Change Password")
                print("deluser     Deletes existing user")
                print("cls         Clears the screen")
                print("exit        Exits the command center\n")
                
            elif choice == '':
                continue    
                
            elif choice == 'exit':
                break
            
            else:
                print(f"\n{choice} not recognized as a command. Type help for more info.")
                main()
                
    except ModuleNotFoundError:
        print("\nModules not found\n")
        
    except FileNotFoundError:
        print("\nThe file does not exist!\n")
        
    except KeyboardInterrupt:
        return "\n"
                
if __name__ == "__main__":
    print("USER COMMANDS:")
    
    try:
        #For this session, we reset the passwd.txt file to remove new users and
        # re add previous users if deleted, also resetting everyones password  
        init.initialize()
        
        main()
    
    except FileNotFoundError:
        print("\nNo such file!\n")
        