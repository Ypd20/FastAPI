import pandas as pd
df = pd.read_csv("C:\\Users\\YASH\\Downloads\\Automobile_data.csv")
company = df.groupby('company')
mileage = company['company','average-mileage'].mean()
print(mileage)