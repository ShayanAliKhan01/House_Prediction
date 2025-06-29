# 🏠 House Price Prediction with Linear Regression

This project predicts house prices using a **Linear Regression** model trained on features like:

- Area (in sq. ft.)
- Number of Floors
- Age of the house

The model was trained using Python libraries like **Pandas**, **scikit-learn**, and **Matplotlib**, and visualized using a scatter plot comparing actual and predicted prices.

---

## 🔍 Observations

Initially, I used a smaller dataset, and the model showed an unexpected trend: **older houses were getting higher predicted prices**. This indicated poor generalization due to insufficient or skewed data.

After switching to a **larger, more realistic dataset**, the model's predictions became more logical and aligned with market behavior — showing the real impact of **data quality and size** in machine learning.

---

## 🧠 Tech Stack

- Python
- pandas
- scikit-learn
- matplotlib

---

## 📈 Output Visualization

![Scatter Plot](assets/actual_vs_predicted.png)

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/yourusername/House_Prediction.git
   cd House_Prediction
