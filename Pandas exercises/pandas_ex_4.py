import pandas as pd
df = pd.read_csv("C:\\Users\\YASH\\Downloads\\Automobile_data.csv")
car_Manufacturers = df.groupby('company')
toyotaDf = car_Manufacturers.get_group('toyota')
print(toyotaDf)
