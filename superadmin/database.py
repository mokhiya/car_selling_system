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
        vin VARCHAR(50) NOT NULL UNIQUE ,
        status VARCHAR(50),
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
