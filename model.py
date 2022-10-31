import numpy as np
import pandas_datareader as web
import datetime as dt
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras

crypto_currency = "BTC"
against_currency = "USD"
prediction_days = 60


# getting the data or price of bitcoin
start = dt.datetime(2016, 1, 1)
end = dt.datetime.now()


scaler = MinMaxScaler(feature_range=(0, 1))

model = keras.models.load_model('btc_price_prediction.h5')

# getting the actual price of btc
test_start = dt.datetime(2020, 1, 1)
test_end = dt.datetime.now()
test_data = web.DataReader(f"{crypto_currency}-{against_currency}", "yahoo", test_start, test_end)
actual_prices = test_data["Close"].values

model_inputs = actual_prices.reshape(-1, 1)
model_inputs = scaler.fit_transform(model_inputs)

# spliting the data and predicting 
x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x - prediction_days : x, 0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

prediction_prices = model.predict(x_test)
prediction_prices = scaler.inverse_transform(prediction_prices)

real_data = [model_inputs[len(model_inputs) + 1 - prediction_days : len(model_inputs)+1,0]]
real_data = np.array(real_data)
real_data = np.reshape(real_data,(real_data.shape[0],real_data.shape[1],1))

prediction = model.predict(real_data)
prediction = scaler.inverse_transform(prediction)
print(prediction)


