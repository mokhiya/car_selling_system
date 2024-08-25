from decimal import Decimal
from configs.db_settings import execute_query

def sell_car(branch_id):
    """
    This function handles selling a car to a client.
    """
    while True:
        print("\nSell a Car:")
        print("1. Sell a car to a client")
        print("2. Choose payment method (full or credit)")
        print("3. Back to Seller Menu")
        choice = input("Select an option: ")

        if choice == "1":
            car_id = int(input("Enter the ID of the car you want to sell: "))
            selected_car_query = "SELECT id, name, price FROM cars WHERE id = %s AND branches_id = %s"
            selected_car = execute_query(selected_car_query, (car_id, branch_id), fetch="one")
            
            if selected_car:
                payment_method = input("Choose payment method (full or credit): ").lower()
                
                if payment_method == "full":
                    delete_car_query = "DELETE FROM cars WHERE id = %s AND branches_id = %s"
                    execute_query(delete_car_query, (car_id, branch_id))
                    print("Car sold successfully!")
                elif payment_method == "credit":
                    print("Credit sale process initiated.")
                else:
                    print("Invalid payment method.")
            else:
                print("Car ID not found or does not belong to this branch.")
        elif choice == "2":
            print("Choosing payment method...")
        elif choice == "3":
            break
        else:
            print("Invalid choice, please try again.")

def view_sales_history(branch_id):
    query = """
    SELECT sales.id, cars.name, sales.payment_method, sales.sale_date, sales.amount 
    FROM sales 
    JOIN cars ON sales.car_id = cars.id 
    WHERE sales.branch_id = %s
    """
    sales = execute_query(query, (branch_id,), fetch="all")
    
    if not sales:
        print("No sales history found.")
    else:
        print("Sales History:")
        for sale in sales:
            print(f"Sale ID: {sale[0]}, Car: {sale[1]}, Payment Method: {sale[2]}, Date: {sale[3]}, Amount: {sale[4]}")

def view_available_cars(branch_id):
    query = "SELECT id, name, price FROM cars WHERE branches_id = %s"
    cars = execute_query(query, (branch_id,), fetch="all")
    
    if not cars:
        print("No cars available.")
    else:
        print("Available Cars:")
        for car in cars:
            print(f"ID: {car[0]}, Name: {car[1]}, Price: {car[2]}")
