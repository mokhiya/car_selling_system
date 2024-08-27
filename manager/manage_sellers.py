from configs.db_settings import execute_query
from common import print_enumerate

def create_seller_account():
    """
    Create a new seller account in the database.

    This function inserts a new record into the 'employees' table with the provided
    seller details. The new seller is assigned a user type of 'seller' and is marked
    as active by default.
    """
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
    """
    Update the details of an existing seller account in the database.

    This function prompts the user to enter the seller's ID and select which field
    (login, password, full name, email, or branch ID) they would like to update.
    """
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
    """
    Update a specific field of a seller account in the database.
    :param seller_id:
    :param field:
    :param new_value:
    :return:
    """
    query = f"""UPDATE employees SET {field} = %s
            WHERE id = %s AND user_type = (SELECT id FROM user_type WHERE name = 'Seller');
            """
    params = (new_value, seller_id)
    execute_query(query, params)
    print("Seller updated successfully.")


def delete_seller_account():
    """
    Delete an existing seller account from the database.

    This function prompts the user to enter the seller's ID and executes an SQL DELETE
    statement to remove the seller account from the 'employees' table.
    :return:
    """
    seller_id = int(input("Enter the seller's ID to delete: "))

    query = """
            DELETE FROM employees 
            WHERE id = %s AND user_type = (SELECT id FROM user_type WHERE name = 'Seller');
            """
    params = (seller_id,)
    execute_query(query, params)
    print("Seller deleted successfully.")


def view_all_sellers_in_branch():
    """
    Retrieve and display all sellers associated with a specific branch.
    :return:
    """
    branch_id = int(input("Enter ID of the branch:  "))

    query = """SELECT full_name, email, is_active FROM employees WHERE branches_id = %s AND 
            user_type = (SELECT id FROM user_type WHERE name = 'Seller');"""
    params = (branch_id,)
    sellers = execute_query(query, params, 'all')

    if not sellers:
        print("No cars available.")
    else:
        print_enumerate(sellers)
