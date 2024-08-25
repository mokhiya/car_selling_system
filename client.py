from decimal import Decimal
from configs.db_settings import execute_query

def view_available_cars():
    query = '''
    SELECT c.id, c.model, b.name AS brand, cl.name AS color, c.year, c.price, c.branches_id
    FROM cars c
    JOIN brands b ON c.brands_id = b.id
    JOIN colors cl ON c.colors_id = cl.id
    '''
    cars = execute_query(query, fetch="all")
    if not cars:
        print("No cars available.")
    else:
        print("Available Cars:")
        for car in cars:
            print(f"Model: {car[1]}, Brand: {car[2]}, Color: {car[3]}, Year: {car[4]}, Price: ${car[5]}, Branches ID: {car[6]}")

def buy_car():
    view_available_cars()
    car_id = int(input("Enter the ID of the car you want to purchase: "))

    query = '''
    SELECT c.id, c.model, b.name AS brand, cl.name AS color, c.year, c.price, c.branches_id
    FROM cars c
    JOIN brands b ON c.brands_id = b.id
    JOIN colors cl ON c.colors_id = cl.id
    WHERE c.id = %s
    '''
    selected_car = execute_query(query, params=(car_id,), fetch="one")
    
    if selected_car:
        print("Purchase Options:")
        print("1. Full Payment")
        print("2. Credit")
        option = input("Choose an option (1/2): ")
        
        if option == '1':
            payment_amount = selected_car[5]
            balance = 0
            print(f"You have purchased {selected_car[1]} ({selected_car[2]} - {selected_car[3]}) for ${payment_amount}.")
        elif option == '2':
            payment_amount = Decimal(input("Enter down payment amount: "))
            balance = Decimal(selected_car[5]) - payment_amount
            print(f"You have purchased {selected_car[1]} ({selected_car[2]} - {selected_car[3]}) on credit.")
            print(f"Down Payment: ${payment_amount}, Balance: ${balance}")
        else:
            print("Invalid option selected.")
            return
        
        insert_query = '''
        INSERT INTO purchases (car_id, make, model, payment_amount, remaining_balance)
        VALUES (%s, %s, %s, %s, %s)
        '''
        execute_query(insert_query, params=(selected_car[0], selected_car[1], selected_car[2], payment_amount, balance))
    else:
        print("Car ID not found.")

def view_purchase_history():
    query = "SELECT * FROM purchases"
    records = execute_query(query, fetch="all")
    if not records:
        print("No purchase history found.")
    else:
        print("Purchase History:")
        for record in records:
            print(f"Car ID: {record[1]}, Make: {record[2]}, Model: {record[3]}, Payment: ${record[4]}, Remaining Balance: ${record[5]}")

def main_menu():
    while True:
        print("\nCar Selling System")
        print("1. Buy a Car")
        print("2. View available cars")
        print("3. View Purchase History")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            buy_car()
        elif choice == '2':
            view_available_cars()
        elif choice == '3':
            view_purchase_history()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
