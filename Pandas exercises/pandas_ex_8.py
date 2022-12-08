import pandas as pd
expensive_cars = pd.read_csv("C:\\Users\\YASH\\Downloads\\Automobile_data.csv")
expensive_cars= expensive_cars.sort_values(by=['price'], ascending=False)
print(expensive_cars.head(5))