import numpy as np
import pandas as pd
from pandas_datareader import data as web
import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go

symbol = input('ticker=')+'.SA'
periodo = '1y'

tickers = yf.Ticker(symbol)
df = tickers.history(period=periodo)
#df = yf.download(ticker+'.SA', period = periodo, auto_ajusted=True)
df["Date"]=df.index
#
# calcular a média de 30 dias
avg_5 = df.Close.rolling(window=9, min_periods=1).mean()
avg_20 = df.Close.rolling(window=21, min_periods=1).mean()
avg_60 = df.Close.rolling(window=72, min_periods=1).mean()
avg_200 = df.Close.rolling(window=250, min_periods=1).mean()


trace1 = {
    'x': df.Date,
    'open': df.Open,
    'close': df.Close,
    'high': df.High,
    'low': df.Low,
    'type': 'candlestick',
 #   'name': 'ITSA',
    'showlegend': False
}
# média de 20 dias (linha)
trace2 = {
    'x': df.Date,
    'y': avg_20,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'orange'
    },
    'name': 'Média (21 dias)'
}
trace3 = {
    'x': df.Date,
    'y': avg_60,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'red'
    },
    'name': 'Média (72 dias)'
}
trace4 = {
    'x': df.Date,
    'y': avg_5,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'blue'
    },
    'name': 'Média (09 dias)'
}
trace5 = {
    'x': df.Date,
    'y': avg_200,
    'type': 'scatter',
    'mode': 'lines',
    'line': {
        'width': 1,
        'color': 'brown'
    },
    'name': 'Média (250 dias)'
}
# informar todos os dados e gráficos em uma lista
data = [trace4,trace1,trace2,trace3,trace5]
 
# configurar o layout do gráfico
layout = go.Layout({
    'title': {
        'text': 'Gráfico de Candlestick',
        'font': {
            'size': 10
        }
    }
})
 
# instanciar objeto Figure e plotar o gráfico
fig = go.Figure(data=data, layout=layout)
fig.show()

