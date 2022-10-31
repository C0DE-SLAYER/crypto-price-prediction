'''
url for using this parameter
http://127.0.0.1:5000/predict?coin_name=btc&days=50
'''

from flask import Flask, request, jsonify
import datetime as dt
import yfinance as yf
from prophet import Prophet
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def ml_model(coin_name,days):
    df = yf.download(f'{coin_name}-USD',dt.date.today() - dt.timedelta(days=365),dt.date.today())
    df.reset_index(inplace=True)
    df = df[['Date','Adj Close']]
    df.columns = ['ds','y']
    try:
        df['ds'] = df['ds'].dt.tz_convert(None)
    except:
        pass
    model = Prophet()
    model.fit(df)
    future_dates = model.make_future_dataframe(periods = days)
    prediction = model.predict(future_dates)
    prediction = prediction[['ds','yhat']]
    return prediction['yhat'].iloc[-1]


@app.route('/')
def home():
    resp = '''
    <h1> crypto price prediction </h1>
    <h3>As the name suggest this api give you predicted peice of top 100 token</h3>
    <p> Api = https://cryptopricepredict.herokuapp.com/ </p>
    <p><u> endpoint</u>: <b> /predict </b> <br> as the name suggest this endpoint will predict price<br>
    there are two required parameter which are 1. coin_name and 2. days<br>
    <b>Example:</b> predict?coin_name=btc&days=50 return a json object with price which is 18.6742932</p>
    '''
    return resp

@app.route('/predict')
@cross_origin()
def predict():
    coin_name = request.args.get('coin_name').upper()
    days_to_predict = int(request.args.get('days'))
    prediction = ml_model(coin_name.upper(),int(days_to_predict))
    return jsonify({"price":prediction})

if __name__ == '__main__':
    app.run(debug=True)
