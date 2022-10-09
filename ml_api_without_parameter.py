from flask import Flask, render_template, request
import requests
import pandas as pd
import datetime as dt
import yfinance as yf
from prophet import Prophet

app = Flask(__name__)

def get_coin_name():
    url = 'https://api.coincap.io/v2/assets'
    data = requests.get(url).json()['data']
    df = pd.DataFrame(data)
    df = df['symbol']
    return df

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

@app.route('/predict', methods = ['GET','POST'])
def predict_without_parameter():
    if request.method == 'POST':
        coin_name = request.form.get('coins')
        days = int(request.form.get('date_pre'))
        prediction = ml_model(coin_name,days)
        return f'The predicted value is {prediction}'
    else:
        coin = get_coin_name()
        return render_template('ml_api_without_parameter.html',coin=coin)



if __name__ == '__main__':
    app.run(debug=True)
