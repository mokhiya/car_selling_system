from configs.db_settings import execute_query
from unicodedata import decimal

from common import print_enumerate


def add_new_car():
    model = input("Enter name of the car: ")
    brands_id = int(input("Enter brand_id of the car:  "))
    colors_id = int(input("Enter color_id of the car:  "))
    year = input("Enter year of the car (YYYY-MM-DD):  ")
    price = decimal("Enter price:  ")
    branches_id = int(input("Enter branch_id:  "))
    vin = input("Enter VIN of the car:  ")

    query = """INSERT INTO cars (model, brands_id, colors_id, year, price, branches_id, vin) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
    params = (model, brands_id, colors_id, year, price, branches_id, vin)

    execute_query(query, params)
    print("Car added successfully.")


def update_car_details():
    car_id = int(input("Enter ID of the car to update: "))

    fields = ['model', 'brands_id', 'colors_id', 'year', 'price', 'branches_id', 'vin']
    print_enumerate(fields)

    choice = int(input("What would you like to update? Enter your choice:  "))
    if choice == 1 or choice == 4 or choice == 7:
        new_value = input(f"Enter new value for {fields[choice - 1]}:  ")
    elif choice == 5:
        new_value = decimal(input(f"Enter new value for {fields[choice - 1]}:  "))
    else:
        new_value = int(input(f"Enter new value for {fields[choice - 1]}:  "))

    update(car_id, fields[choice - 1], new_value)


def update(car_id, field, new_value):
    query = f"UPDATE cars SET {field} = %s WHERE id = %s);"
    params = (new_value, car_id)

    execute_query(query, params)
    print("Car updated successfully.")


def delete_car():
    car_id = int(input("Enter ID of the car to delete: "))

    query = "DELETE FROM cars WHERE id = %s;"
    params = (car_id,)

    execute_query(query, params)
    print("Car deleted successfully.")


def view_available_cars_in_branch():
    branch_id = int(input("Enter ID of the branch:  "))
    query = "SELECT * FROM cars WHERE branches_id = %s;"
    params = (branch_id,)

    execute_query(query, params, 'all')
