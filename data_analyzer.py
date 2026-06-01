import pandas as pd
import matplotlib.pyplot as plt

# 1. Data define karna (Product aur Sales dono columns ke saath)
data = {
    'Product': ['A', 'B', 'C', 'D'], 
    'Sales': [100, 150, 200, 250]
}

# 2. DataFrame banana
df = pd.DataFrame(data)

# 3. Data print karke check karna
print("Data Preview:")
print(df)

# 4. Graph banana (Bar chart)
df.plot(kind='bar', x='Product', y='Sales', color='skyblue')

# Graph ki styling
plt.title('Product Sales Analysis')
plt.xlabel('Product Name')
plt.ylabel('Sales Amount')

# 5. Graph show karna
plt.show()