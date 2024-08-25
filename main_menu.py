from superadmin.database import (create_database,
                                 add_update_or_delete_manager, see_all_managers,
                                 total_sales, total_revenue, sales_per_branch, sales_per_seller)
from seller.seller import (sell_car_menu, view_available_cars, view_sales_history)
from client.client import (view_available_cars, view_purchase_history, buy_car)
from client.registerclient import register_client
from configs.db_settings import execute_query


def check_login(login, password):
    super_admin_login = "super"
    super_admin_password = "super"

    if login == super_admin_login and password == super_admin_password:
        print("Login successful")
        return show_super_admin_menu()

    employee_query = """
    SELECT e.user_type, u.name, e.is_active
    FROM employees e
    JOIN user_type u ON e.user_type = u.id
    WHERE e.login = %s AND e.password = %s;
    """

    employee = execute_query(employee_query, params=(login, password), fetch="one")

    if employee:
        user_type, user_role, is_active = employee

        if not is_active:
            update_query = "UPDATE employees SET is_active = TRUE WHERE login = %s;"
            execute_query(update_query, params=(login,))
            print(f"{user_role} login successful and status updated.")

        if user_role == 'Manager':
            return branch_manager_menu()
        elif user_role == 'Seller':
            return seller_menu()
        else:
            print("Unknown user type.")
            return

    client_query = """
    SELECT is_active
    FROM customers
    WHERE login = %s AND password = %s;
    """

    client = execute_query(client_query, params=(login, password), fetch="one")

    if client:
        is_active = client[0]

        if not is_active:
            update_query = "UPDATE customers SET is_active = TRUE WHERE login = %s;"
            execute_query(update_query, params=(login,))
            print("Client login successful and status updated.")

        return client_query

    print("Invalid login or password. Please try again.")


def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. Register (for new clients only)")
        print("2. Login")
        print("3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            login = input("Login: ")
            password = input("Password: ")
            check_login(login, password)
        elif choice == "2":
            if register_client():
                return client_menu()
        elif choice == "3":
            print("Thank you using for our service!")
            break
        else:
            print("Invalid choice, please try again.")


def show_super_admin_menu():
    """
    This function shows the main menu of the superadmin menu.
    """
    text = input("""
    1. Create database.   
    2. Manager management.
    3. Statistics.
    4. Go to back

    Choose an option above: """)

    if text == "1":
        if create_database():
            return show_super_admin_menu()
    elif text == "2":
        if show_manger_management_menu():
            return show_super_admin_menu()
    elif text == "3":
        if show_statistics_menu():
            return show_super_admin_menu()
    elif text == "4":
        return main_menu()
    else:
        print("Invalid input")
        show_super_admin_menu()


def show_manger_management_menu():
    """
    This function shows the main menu of the manger management menu.
    """
    text = input("""
    1. Add/update/delete manager account.
    2. See all managers.
    3. Go to back.

    Choose an option above: """)

    if text == "1":
        if add_update_or_delete_manager():
            show_manger_management_menu()
    elif text == "2":
        if see_all_managers():
            show_manger_management_menu()
    elif text == "3":
        show_super_admin_menu()
    else:
        print("Invalid input")
        show_manger_management_menu()


def show_statistics_menu():
    """
    This function shows the main menu of the statistics menu.
    """
    text = input("""
    1. Total sales.
    2. Total revenue.
    3. Sales per branch.
    4. Sales per seller. 
    5. Go to back.

    Choose an option above: """)

    if text == "1":
        total_sales()
    elif text == "2":
        total_revenue()
    elif text == "3":
        sales_per_branch()
    elif text == "4":
        sales_per_seller()
    elif text == "5":
        return show_super_admin_menu()
    else:
        print("Invalid input")
        show_statistics_menu()


def branch_manager_menu():
    """
    This function shows the main menu of the branch management menu.
    """
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
            main_menu()
        else:
            print("Invalid choice, please try again.")


def manage_sellers_menu():
    """
    This function shows the main menu of the sellers menu.
    """
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
    """
    This function shows the main menu of the cars menu.
    """
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


def seller_menu(branch_id):
    while True:
        print("\nSeller Menu:")
        print("1. Sell a Car")
        print("2. View Sales History")
        print("3. View Available Cars")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sell_car_menu(branch_id)
        elif choice == '2':
            view_sales_history(branch_id)
        elif choice == '3':
            view_available_cars(branch_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")



def client_menu():
    """
    This function shows the main menu of the client menu.
    """
    while True:
        print("\nClient Menu:")
        print("1. Buy a Car")
        print("2. View Purchase History")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            if buy_car_menu():
                return client_menu
        elif choice == "2":
            view_purchase_history
        elif choice == "3":
            main_menu()
        else:
            print("Invalid choice, please try again.")

def buy_car_menu():
    """
    This function shows the main menu for buying a car.
    """
    while True:
        print("\nBuy a Car:")
        print("1. View available cars")
        print("2. Purchase a car (full or credit)")
        print("3. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == "1":
            view_available_cars()
        elif choice == "2":
            buy_car()
        elif choice == "3":
            main_menu()
        else:
            print("Invalid choice, please try again.")