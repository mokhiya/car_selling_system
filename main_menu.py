def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def super_admin_menu():
    while True:
        print("\nSuper Admin Menu:")
        print("1. Manage Branch Managers")
        print("2. View System Statistics")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            manage_branch_managers()
        elif choice == "2":
            view_system_statistics()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def manage_branch_managers():
    while True:
        print("\nManage Branch Managers:")
        print("1. Create branch manager account")
        print("2. Update branch manager account")
        print("3. Delete branch manager account")
        print("4. View all branch managers")
        print("5. Back to Super Admin Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def view_system_statistics():
    while True:
        print("\nView System Statistics:")
        print("1. Total sales")
        print("2. Total revenue")
        print("3. Sales per branch")
        print("4. Sales per seller")
        print("5. Back to Super Admin Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def branch_manager_menu():
    while True:
        print("\nBranch Manager Menu:")
        print("1. Manage Sellers")
        print("2. Manage Cars")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            manage_sellers_menu()
        elif choice == "2":
            manage_cars_menu()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def manage_sellers_menu():
    while True:
        print("\nManage Sellers:")
        print("1. Create seller account")
        print("2. Update seller account")
        print("3. Delete seller account")
        print("4. View all sellers in branch")
        print("5. Back to Branch Manager Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def manage_cars_menu():
    while True:
        print("\nManage Cars:")
        print("1. Add a new car")
        print("2. Update car details")
        print("3. Delete car")
        print("4. View available cars in branch")
        print("5. Back to Branch Manager Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            pass
        elif choice == "5":
            break
        else:
            print("Invalid choice, please try again.")

def seller_menu():
    while True:
        print("\nSeller Menu:")
        print("1. Sell a Car")
        print("2. View sales history")
        print("3. View Available Cars")
        print("4. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            sell_car()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

def sell_car():
    while True:
        print("\nSell a Car:")
        print("1. Sell a car to a client")
        print("2. Choose payment method (full or credit)")
        print("3. Back to Seller Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def client_menu():
    while True:
        print("\nClient Menu:")
        print("1. Buy a Car")
        print("2. View Purchase History")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            buy_car_menu()
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def buy_car_menu():
    while True:
        print("\nBuy a Car:")
        print("1. View available cars")
        print("2. Purchase a car (full or credit)")
        print("3. Back to Client Menu")
        choice = input("Select an option: ")

        if choice == "1":
            pass
        elif choice == "2":
            pass
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()
