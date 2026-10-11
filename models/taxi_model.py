
'''Defines the data model for taxi-related information.'''

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error
from joblib import dump
import pandas as pd

DATASET_PATH = 'dataset\\synthetic_delivery_dataset.csv'

data = pd.read_csv(DATASET_PATH)

X = data[['distance', 'traffic']]
y = data['price']

X_train, X_test, y_train, y_test = train_test_split(X.values, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

pre = model.predict(X_test)

r2 = r2_score(y_test, pre)
mae = mean_absolute_error(y_test, pre)
print(f'R2 SCORE: {round(r2, 2)}')
print(f'MAE: {round(mae, 2)}')

print()
print(f'PREDICT MACHINE: {round(model.predict([[3, 1]])[0], 1)} IRR')

# Export Model
try:
    dump(model, 'models/trained/model-trained-v1.0.1.pkl')
except Exception as e:
    print(e)
