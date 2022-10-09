'''
url for using this parameter
http://127.0.0.1:5000/predict?coin_name=btc&days=50
'''

from flask import Flask, request
import datetime as dt
import yfinance as yf
from prophet import Prophet

app = Flask(__name__)

def ml_model(coin_name,days):
    df = yf.download(f'{coin_name}-USD',dt.date.today() - dt.timedelta(days=365),dt.date.today())
    df.reset_index(inplace=True)
    df = df[['Date','Adj Close']]
    df.columns = ['ds','y']
    model = Prophet()
    model.fit(df)
    future_dates = model.make_future_dataframe(periods = days)
    prediction = model.predict(future_dates)
    prediction = prediction[['ds','yhat']]
    return prediction['yhat'].iloc[-1]

@app.route('/predict')
def predict():
    coin_name = request.args.get('coin_name')
    days_to_predict = request.args.get('days')
    prediction = ml_model(coin_name.upper(),int(days_to_predict))
    return f'The predicted value is {prediction}'

if __name__ == '__main__':
    app.run(debug=True)
