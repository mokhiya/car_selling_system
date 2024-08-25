from configs.db_settings import execute_query


def create_database():
    query = """
    CREATE TABLE user_type (
        id BIGINT PRIMARY KEY,
        name VARCHAR(50) NOT NULL
    ),
    CREATE TABLE customers (
        id BIGSERIAL PRIMARY KEY,
        login VARCHAR(64) NOT NULL,
        password VARCHAR(64) NOT NULL,
        full_name VARCHAR(128) NOT NULL,
        email VARCHAR(128) NOT NULL UNIQUE,
        is_active BOOLEAN DEFAULT FALSE,
    ),
    CREATE TABLE employees (
        id BISERIAL PRIMARY KEY,
        login VARCHAR(64) NOT NULL,
        password VARCHAR(64) NOT NULL,
        full_name VARCHAR(128) NOT NULL,
        email VARCHAR(128),
        user_type BIGINT,
        is_active BOOLEAN DEFAULT FALSE,
        branches_id BIGINT,
        FOREIGN KEY (user_type) REFERENCES user_type(id),
        FOREIGN KEY (branches_id) REFERENCES branches(id)
    ),
    CREATE TABLE branches (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(128) NOT NULL,
        location VARCHAR(100) NOT NULL
    ),
    CREATE TABLE brands (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL UNIQUE 
    ),
    CREATE TABLE colors (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE 
    ),
    CREATE TABLE cars (
        id BIGSERIAL PRIMARY KEY,
        model VARCHAR(128) NOT NULL,
        brands_id BIGINT,
        colors_id BIGINT,
        year INT,
        price DECIMAL,
        branches_id BIGINT,
        vin VARCHAR(50) NOT NULL UNIQUE ,
        status VARCHAR(50),
        FOREIGN KEY (brands_id) REFERENCES brands(id),
        FOREIGN KEY (colors_id) REFERENCES colors(id),
        FOREIGN KEY (branches_id) REFERENCES branches(id)
    ), 
    CREATE TABLE sale_type (
        id BIGSERIAL PRIMARY KEY,
        type VARCHAR(64) NOT NULL
    ), 
    CREATE TABLE payment_method (
        id BIGSERIAL PRIMARY KEY,
        name VARCHAR(64) NOT NULL
    ),
    CREATE TABLE sales (
        id BIGSERIAL PRIMARY KEY,
        customer_id BIGINT,
        cars_id BIGINT,
        sale_type_id BIGINT,
        amount BIGINT,
        sale_date DATE,
        payment_method_id BIGINT,
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (cars_id) REFERENCES cars(id),
        FOREIGN KEY (sale_type_id) REFERENCES sale_type(id),
        FOREIGN KEY (payment_method_id) REFERENCES payment_method(id)
    );
    """

    execute_query(query)
    print("Database created successfully")


def add_update_or_delete_manager():
    action = input("Would you like to add, update, or delete a manager? (add/update/delete): ").strip().lower()

    if action == "add":
        login = input("Enter manager's login: ")
        password = input("Enter manager's password: ")
        full_name = input("Enter manager's full name: ")
        email = input("Enter manager's email: ")
        branches_id = input("Enter the branch ID: ")

        query = """
        INSERT INTO employees (login, password, full_name, email, user_type, is_active, branches_id)
        VALUES (%s, %s, %s, %s, (SELECT id FROM user_type WHERE name = 'Manager'), TRUE, %s);
        """
        params = (login, password, full_name, email, branches_id)
        execute_query(query, params)
        print("Manager added successfully.")

    elif action == "update":
        manager_id = input("Enter the manager's ID to update: ")
        update_field = input(
            "What would you like to update? (login/password/full_name/email/branches_id): ").strip().lower()
        new_value = input(f"Enter new value for {update_field}: ")

        query = f"""
        UPDATE employees 
        SET {update_field} = %s 
        WHERE id = %s AND user_type = (SELECT id FROM user_type WHERE name = 'Manager');
        """
        params = (new_value, manager_id)
        execute_query(query, params)
        print("Manager updated successfully.")

    elif action == "delete":
        manager_id = input("Enter the manager's ID to delete: ")

        query = """
        DELETE FROM employees 
        WHERE id = %s AND user_type = (SELECT id FROM user_type WHERE name = 'Manager');
        """
        params = (manager_id,)
        execute_query(query, params)
        print("Manager deleted successfully.")

    else:
        print("Invalid action. Please choose 'add', 'update', or 'delete'.")
        add_update_or_delete_manager()


def see_all_managers():
    query = """
    SELECT e.id, e.login, e.full_name, e.email, b.name AS branch_name
    FROM employees e
    JOIN branches b ON e.branches_id = b.id
    WHERE e.user_type = (SELECT id FROM user_type WHERE name = 'Manager');
    """

    try:
        managers = execute_query(query, fetch="all")

        if managers:
            print("\nList of Managers:")
            print("ID | Login | Full Name | Email | Branch")
            print("-" * 50)
            for manager in managers:
                print(f"{manager[0]} | {manager[1]} | {manager[2]} | {manager[3]} | {manager[4]}")
        else:
            print("No managers found.")

    except Exception as e:
        print(f"An error occurred: {e}")
