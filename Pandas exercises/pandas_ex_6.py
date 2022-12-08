import pandas as pd
df = pd.read_csv("C:\\Users\\YASH\\Downloads\\Automobile_data.csv")
company = df.groupby('company')
price = company['company','price'].max()
print(price)