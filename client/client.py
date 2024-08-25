from decimal import Decimal, InvalidOperation
from configs.db_settings import execute_query
from datetime import datetime


def view_available_cars():
    """
    Fetch and display available cars from the database.
    """
    query = '''
    SELECT
        c.id,
        c.name,
        b.name AS brand,
        cl.name AS color,
        c.year,
        c.price,
        br.name AS branch
    FROM
        cars c
    JOIN
        brands b ON c.brands_id = b.id
    JOIN
        colors cl ON c.colors_id = cl.id
    JOIN
        branches br ON c.branches_id = br.id
    ORDER BY
        c.id
    '''
    cars = execute_query(query, fetch='all')
    if not cars:
        print("\nNo cars available.\n")
    else:
        print("\nAvailable Cars:")
        print("-" * 80)
        for car in cars:
            print(f"ID: {car[0]}")
            print(f"Name: {car[1]}")
            print(f"Brand: {car[2]}")
            print(f"Color: {car[3]}")
            print(f"Year: {car[4]}")
            print(f"Price: ${car[5]:,.2f}")
            print(f"Branch: {car[6]}")
            print("-" * 80)


def buy_car():
    """
    Handle the car purchase process, allowing users to choose payment options.
    """
    view_available_cars()
    try:
        car_id = int(input("Enter the ID of the car you want to purchase: "))
    except ValueError:
        print("Invalid input. Please enter a valid car ID.")
        return

    query = '''
    SELECT
        c.id,
        c.name,
        b.name AS brand,
        cl.name AS color,
        c.year,
        c.price,
        br.name AS branch
    FROM
        cars c
    JOIN
        brands b ON c.brands_id = b.id
    JOIN
        colors cl ON c.colors_id = cl.id
    JOIN
        branches br ON c.branches_id = br.id
    WHERE
        c.id = %s
    '''
    selected_car = execute_query(query, params=(car_id,), fetch='one')

    if selected_car:
        print("\nPurchase Options:")
        print("1. Full Payment")
        print("2. Credit")
        option = input("Choose an option (1/2): ")

        if option == '1':
            payment_amount = selected_car[5]
            remaining_balance = Decimal('0.00')
            print(f"\nYou have purchased {selected_car[1]} ({selected_car[2]} - {selected_car[3]}) for ${payment_amount:,.2f}.")

        elif option == '2':
            try:
                down_payment = Decimal(input("Enter down payment amount: "))
                if down_payment <= 0 or down_payment > selected_car[5]:
                    print("Invalid down payment amount.")
                    return
                remaining_balance = selected_car[5] - down_payment
                payment_amount = down_payment
                print(f"\nYou have purchased {selected_car[1]} ({selected_car[2]} - {selected_car[3]}) on credit.")
                print(f"Down Payment: ${payment_amount:,.2f}")
                print(f"Remaining Balance: ${remaining_balance:,.2f}")
            except (InvalidOperation, ValueError):
                print("Invalid input. Please enter a valid amount.")
                return
        else:
            print("Invalid option selected.")
            return

        insert_query = '''
        INSERT INTO purchases (
            car_id,
            car_name,
            brand,
            color,
            year,
            price,
            branch,
            payment_amount,
            remaining_balance,
            purchase_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''
        params = (
            selected_car[0],
            selected_car[1],
            selected_car[2],
            selected_car[3],
            selected_car[4],
            selected_car[5],
            selected_car[6],
            payment_amount,
            remaining_balance,
            datetime.now()
        )
        execute_query(insert_query, params=params)
        print("Purchase recorded successfully.")
    else:
        print("Car ID not found.")


def view_purchase_history():
    """
    Display the purchase history from the purchases table.
    """
    query = '''
    SELECT
        id,
        car_name,
        brand,
        color,
        year,
        price,
        branch,
        payment_amount,
        remaining_balance,
        purchase_date
    FROM
        purchases
    ORDER BY
        purchase_date DESC
    '''
    records = execute_query(query, fetch='all')
    if not records:
        print("\nNo purchase history found.\n")
    else:
        print("\nPurchase History:")
        print("-" * 100)
        for record in records:
            print(f"Purchase ID: {record[0]}")
            print(f"Car Name: {record[1]}")
            print(f"Brand: {record[2]}")
            print(f"Color: {record[3]}")
            print(f"Year: {record[4]}")
            print(f"Price: ${record[5]:,.2f}")
            print(f"Branch: {record[6]}")
            print(f"Payment Amount: ${record[7]:,.2f}")
            print(f"Remaining Balance: ${record[8]:,.2f}")
            print(f"Purchase Date: {record[9].strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 100)


def buy_car_menu():
    """
    Show the buy car menu and handle user choices.
    """
    while True:
        print("\nBuy a Car Menu:")
        print("1. View available cars")
        print("2. Purchase a car (full or credit)")
        print("3. Back to Client Menu")
        choice = input("Select an option: ")

        if choice == "1":
            view_available_cars()
        elif choice == "2":
            buy_car()
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")
