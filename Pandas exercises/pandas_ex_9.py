import pandas as pd
german_cars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
german_cars_df = pd.DataFrame.from_dict(german_cars)

japanese_cars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
japanese_cars_df = pd.DataFrame.from_dict(japanese_cars)

cars = pd.concat([german_cars_df, japanese_cars_df], keys=["Germany", "Japan"])
print(cars)