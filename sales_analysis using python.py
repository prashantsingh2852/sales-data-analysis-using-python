# %%
import pandas as pd

# %%
data = pd.read_csv("all_data.csv")

# %%
data.head()

# %%
### To check how much null values we have in the overall dataset

# %%
data.isnull().sum()

# %%
### To drop the NaN rows

# %%
data = data.dropna()

data.isnull().sum()  ## To check the updated NaN values

# %%
## To extract the Order month from the Order data expression

# %%
data['sales_month'] = data['Order Date'].str[0:2]

# %%
## To check the list of all columns present in the dataset

# %%
data.columns

# %%
## To filter out NaN rows and set the same as a new dataset

# %%
data = data[data['sales_month'] != 'Or']
data

# %%
## To convert datatype from object to int

# %%
data['sales_month'] = data['sales_month'].astype(int)  #Object to INT

# %%
data['Quantity Ordered'] = data['Quantity Ordered'].astype(int)  #Object to INT

# %%
data['Price Each'] = data['Price Each'].astype(float) #Object to float

# %%
data['Order Date'] = pd.to_datetime(data['Order Date']) #Object to datatime

# %%
## Calculated field

# %%
data['sales'] = data['Quantity Ordered'] * data['Price Each']

# %%
data.head()

# %%
## Question 1: What was the best month for the sales ?

# %%
sales_by_month = data.groupby('sales_month')['sales'].sum()

sales_by_month

# %%
import matplotlib.pyplot as plt

# %%
month = list(range(1,13))
month

# %%
plt.bar(month,sales_by_month)
plt.show()

# %%
data.head()

# %%
## How to split a string into multiple columns then select only the required ones

# %%
data['city'] = data['Purchase Address'].str.split(',',expand = True)[1]

# %%
## How to split a string and then trim to get the necessary value

# %%
data['state'] = data['Purchase Address'].str.split(',',expand = True)[2]

data['state'] = data['state'].str.strip().str[:-6]

data.head()

# %%
## Question 2: What city has the highest number of sales ?

# %%
sales_by_city = data.groupby('city')['sales'].sum()

sales_by_city

# %%
city = [city for city, df in data.groupby('city')]
city

# %%
plt.figure(figsize=(10,8))
plt.bar(city,sales_by_city)
plt.xticks(rotation = 'vertical',size = 8)
plt.xlabel('city_name')
plt.ylabel('total_sales ($)')
plt.title('total_sales / city')
plt.show()

# %%
 ## What time should we display advertisemets to maximize the likelihood of customer buying the products ?

# %%
data['hour'] = data['Order Date'].dt.hour
data.head()

# %%
order_by_hour = data.groupby('hour')['Order ID'].count()
order_by_hour

# %%
range_hour = list(range(0,24))
range_hour

# %%
plt.figure(figsize=(8,5))
plt.plot(range_hour,order_by_hour)
plt.xticks(range_hour)
plt.xlabel('hour')
plt.ylabel('order_by_hour')
plt.grid()
plt.show()

# %%
## What products are most often sold together ?

# %%
## Creating a new dataset to group all the duplicated orders in order to get the set of products which are purchased together

# %%
temp_data = data[data['Order ID'].duplicated(keep = False)]
temp_data.head()

# %%
temp_data['grouped_product'] = temp_data.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))

temp_data_02 = temp_data[['Order ID','grouped_product']].drop_duplicates().reset_index()

temp_data_02.head()

# %%
from itertools import combinations
from collections import Counter

# %%
count = Counter()

for row in temp_data_02['grouped_product']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

for key, value in count.most_common(10):
    print(key,value)

# %%
## What product sold the most ? Why do you think it sold the most ?

# %%
data.head()

# %%
## Grouping products based on total quantity ordered

# %%
most_qnt_product = data.groupby('Product')['Quantity Ordered'].sum()


most_qnt_product



# %%
products = [Product for Product, df in data.groupby('Product')]

products

# %%
fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.bar(products,most_qnt_product,color = 'g')
ax2.plot(products,avg_price,color = 'b')
ax1.set_xticklabels(products, rotation = 'vertical')
ax1.set_xlabel('Product Name')
ax1.set_ylabel('Total Qty Ordered')
ax2.set_ylabel('Average Price / Product')
plt.show()


# %%



