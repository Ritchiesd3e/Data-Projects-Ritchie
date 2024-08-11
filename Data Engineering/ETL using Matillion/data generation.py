import pandas as pd
import numpy as np
from faker import Faker
import random

fake = Faker()

# Generate Customers Data
customers = pd.DataFrame({
    'customer_id': range(1, 51),
    'first_name': [fake.first_name() for _ in range(50)],
    'last_name': [fake.last_name() for _ in range(50)],
    'email': [fake.email() for _ in range(50)],
    'phone_number': [fake.phone_number() for _ in range(50)],
    'state': [fake.state() for _ in range(50)]  # Added state column
})

# Generate Shops Data
shops = pd.DataFrame({
    'shop_id': range(1, 51),
    'shop_name': [f'Shop {chr(65+i)}' for i in range(50)],
    'location': [fake.city() for _ in range(50)],
    'state': [fake.state() for _ in range(50)]  # Added state column
})

# Generate Orders Data
orders = pd.DataFrame({
    'order_id': range(1, 51),
    'customer_id': [random.randint(1, 50) for _ in range(50)],
    'shop_id': [random.randint(1, 50) for _ in range(50)],
    'order_date': [fake.date_this_year() for _ in range(50)],
    'amount': [round(random.uniform(50, 300), 2) for _ in range(50)],
    'state': [fake.state() for _ in range(50)]  # Added state column
})

# Save to CSV files
customers.to_csv('customers.csv', index=False)
shops.to_csv('shops.csv', index=False)
orders.to_csv('orders.csv', index=False)

import pandas as pd

# Load the CSV files
customers = pd.read_csv('customers.csv')
shops = pd.read_csv('shops.csv')
orders = pd.read_csv('orders.csv')
