import pandas as pd
df = pd.read_csv("C:\\Users\\YASH\\Downloads\\Automobile_data.csv")
print(df['company'].value_counts())