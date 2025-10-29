import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df = pd.read_csv('housing.csv')
print("Housing Data:")
print(df)

X = df[['size', 'bedrooms']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

sample_house = [[1700, 3]]
predicted_price = model.predict(sample_house)
print(f"\nPredicted price for house (Size: {sample_house[0][0]}, Bedrooms: {sample_house[0][1]}): {predicted_price[0]:.2f}")
plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['size'], df['price'], c=df['bedrooms'], cmap='viridis', edgecolor='k', s=100)
plt.colorbar(scatter, label='Number of Bedrooms')
size_range = pd.DataFrame({
    'size': range(int(df['size'].min()), int(df['size'].max())+1, 100),
    'bedrooms': [df['bedrooms'].median()] * (int((df['size'].max() - df['size'].min())/100) + 1)
})
price_pred = model.predict(size_range)
plt.plot(size_range['size'], price_pred, color='red', linewidth=2, label='Regression Line')
plt.xlabel('House Size (sqft)')
plt.ylabel('Price')
plt.title('Housing Price Prediction')
plt.legend()
plt.tight_layout()
chart_path = 'regression_chart.png'
plt.savefig(chart_path)
print(f"\nChart saved at: {os.path.abspath(chart_path)}")
plt.show()
