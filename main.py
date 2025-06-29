import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


df = pd.read_csv("realistic_house_data_with_floors.csv")

x = df[['Area', 'Floors', 'Age']]
y = df['Price']

model = LinearRegression()
model.fit(x,y)

y_pred = model.predict(x)

plt.scatter(y, y_pred, color='blue', alpha=0.7)
plt.plot([y.min(), y.max()], [y.min(), y.max()], color='red')
plt.xlabel("Actual Price (PKR)")
plt.ylabel("Predicted Price (PKR)")
plt.title("Actual vs Predicted House Prices")
plt.grid(True)
plt.show()

print(model.coef_)

input_data = [[1200, 5 ,3]]

predicted_price = model.predict(input_data)
print("Predicted Price:", predicted_price[0])
