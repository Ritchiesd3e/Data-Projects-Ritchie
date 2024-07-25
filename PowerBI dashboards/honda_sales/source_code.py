# Fucntions to create sample data for the Honda cars for PowerBI dashboard:
import pandas as pd
import random
from faker import Faker

# Initialize Faker for generating random data
fake = Faker()

# Define the columns for the CSV
columns = ['Date', 'Car Model', 'Salesperson', 'Customer Name', 'Quantity Sold', 'Sale Price', 'Total Revenue']

# Define some car models and salespeople for more realistic data
car_models = ['Hondo Civic', 'Hondo Accord', 'Hondo CR-V', 'Hondo Pilot', 'Hondo Fit','Honda Amaze']
salespeople = ['Alice Johnson', 'Bob Smith', 'Charlie Davis', 'Dana Lee', 'Evan Martin','Hendry','William Thomson','John']

# Generate 300 rows of data
data = []
for _ in range(500):
    date = fake.date_between(start_date='-1y', end_date='today')
    car_model = random.choice(car_models)
    salesperson = random.choice(salespeople)
    customer_name = fake.name()
    quantity_sold = random.randint(1, 2)
    sale_price = round(random.uniform(500000, 1000000))
    total_revenue = quantity_sold * sale_price
    data.append([date, car_model, salesperson, customer_name, quantity_sold, sale_price, total_revenue])

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Display the final dataframe to download the csv output
df.display()
