import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the data from the spreadsheet
data = pd.read_excel('C:/Users/neitz/Downloads/baseball.xlsx')

# Select the features (team values) and the target variable (playoffs)
features = data[['Runs Scored', 'Runs Allowed', 'Wins', 'OBP', 'SLG', 'Team Batting Average']]
target = data['Playoffs']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Print the predictions
if predictions[0] == 1:
    print("MIL Brewers will make the playoffs")
else:
    print("MIL Brewers will not make the playoffs")
    print("The prediction model is only 80 percent acccuate, so the Brewers may still make the playoffs!!")