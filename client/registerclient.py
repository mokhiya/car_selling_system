from configs.db_settings import execute_query


def register_client():
    """
    This function is used to register a new client to database
    """
    print("Registering a new client...")

    login = input("Enter login: ")
    password = input("Enter password: ")
    full_name = input("Enter full name: ")
    email = input("Enter email: ")

    query = """
    INSERT INTO customers (login, password, full_name, email)
    VALUES (%s, %s, %s, %s);
    """

    try:
        execute_query(query, params=(login, password, full_name, email))
        print("Client registered successfully.")
    except Exception as e:
        print(f"Failed to register client: {e}")
