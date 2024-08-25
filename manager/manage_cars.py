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
