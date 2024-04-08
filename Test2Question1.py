import pandas as pd
import statsmodels.api as sm

# Load the dataset
file_path = r'C:\Users\neitzkeml17\Downloads\Restaurant Revenue.xlsx'
data = pd.read_excel(file_path)

# Extract features and target variable
X = data[['Number_of_Customers', 'Menu_Price', 'Marketing_Spend', 'Average_Customer_Spending', 'Promotions', 'Reviews']]
y = data['Monthly_Revenue']

# Add constant term to the features
X = sm.add_constant(X)

# Fit the OLS (Ordinary Least Squares) model
model = sm.OLS(y, X).fit()

# Print regression statistics
print(model.summary())