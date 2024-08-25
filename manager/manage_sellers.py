from configs.db_settings import execute_query
from common import print_enumerate

def create_seller_account():
    login = input("Enter seller's login: ")
    password = input("Enter seller's password: ")
    full_name = input("Enter seller's full name: ")
    email = input("Enter seller's email: ")
    branch_id = int(input("Enter the branch ID: "))

    query = """
            INSERT INTO employees (login, password, full_name, email, user_type, is_active, branches_id)
            VALUES (%s, %s, %s, %s, (SELECT id FROM user_type WHERE name = 'Seller'), TRUE, %s);
            """
    params = (login, password, full_name, email, branch_id)
    execute_query(query, params)
    print("Seller added successfully.")


def update_seller_account():
    seller_id = int(input("Enter the seller's ID to update: "))

    fields = ['login', 'password', 'full_name', 'email', 'branches_id']
    print_enumerate(fields)

    choice = int(input("What would you like to update? Enter your choice:  "))
    if choice == 5:
        new_value = int(input(f"Enter new value for {fields[choice - 1]}:  "))
    else:
        new_value = input(f"Enter new value for {fields[choice - 1]}:  ")

    update(seller_id, fields[choice - 1], new_value)


def update(seller_id, field, new_value):
    query = f"""UPDATE employees SET {field} = %s
            WHERE id = %s AND user_type = (SELECT id FROM user_type WHERE name = 'Seller');
            """
    params = (new_value, seller_id)
    execute_query(query, params)
    print("Seller updated successfully.")


def delete_seller_account():
    seller_id = int(input("Enter the seller's ID to delete: "))

    query = """
            DELETE FROM employees 
            WHERE id = %s AND user_type = (SELECT id FROM user_type WHERE name = 'Seller');
            """
    params = (seller_id,)
    execute_query(query, params)
    print("Seller deleted successfully.")


def view_all_sellers_in_branch():
    branch_id = int(input("Enter ID of the branch:  "))

    query = """SELECT * FROM employees WHERE branches_id = %s AND 
            user_type = (SELECT id FROM user_type WHERE name = 'Seller');"""
    params = (branch_id,)
    execute_query(query, params, 'all')
