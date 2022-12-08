import pandas as pd
price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
price_df = pd.DataFrame.from_dict(price)

horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182 , 160]}
horsepower_df = pd.DataFrame.from_dict(horsepower)

cars = pd.merge(price_df, horsepower_df, on="Company")
print(cars)