import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from data import get_dataset



def set_training():
    ds = get_dataset()
    features = ['open', 'high', 'low', 'volume']
    training = ds[features]
    y = ds.close

    x_training, x_test, y_training, y_test = train_test_split(training, y, random_state=42)

    # Create model
    lr_model = LinearRegression()
    lr_model.fit(x_training, y_training)

    predict = lr_model.predict(x_test)
    RMSE = mean_squared_error(y_test, predict) ** 0.5

    # Compare real data with predict data
    # print(y_test[:5])
    # print(predict[:5])

    x = ds.date
    real_data = go.Scatter(
        x=x,
        y=y_test,
        # mode='markers',
        name='Preço real'
    )

    predict_data = go.Scatter(
        x=x,
        y=predict,
        name='Preço Estimado'
    )

    layout = go.Layout(
        xaxis=dict(
            title='Data'
        ),
        yaxis=dict(
            range=[x, y],
            title='Valor da ação'
        ),
        showlegend=True
    )
    data = [real_data, predict_data]
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/training')

    # print(y_test)
    # print(predict)
    # print(RMSE)

def predict_prices():
    ds = get_dataset()
    ds['day'] = pd.to_datetime(ds['date']).dt.day
    days = ['day']
    training = ds[days]

    dates = ds.day
    dates_index = training.set_index(ds.day)
    prices = ds.close

    dates2 = np.reshape(dates_index, (len(dates_index), 1))

    # svr_lin = SVR(kernel='linear', C=1000)
    # svr_poly = SVR(kernel='poly', C=1000, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1000, gamma=0.1)

    # svr_lin.fit(dates2, prices)
    # svr_poly.fit(dates2, prices)
    svr_rbf.fit(dates2, prices)

    real_data = go.Scatter(
        x=ds['day'],
        y=prices,
        mode='markers',
        name='Preço real'
    )
    # lin = go.Scatter(
    #     x=ds['day'],
    #     y=svr_lin.predict(dates2),
    #     name='Linear'
    # )
    # poly = go.Scatter(
    #     x=ds['day'],
    #     y=svr_poly.predict(dates2),
    #     name='Poly'
    # )
    rbf = go.Scatter(
        x=ds['day'],
        y=svr_rbf.predict(dates2),
        name='RBF'
    )

    layout = go.Layout(
        xaxis=dict(
            title='Data'
        ),
        yaxis=dict(
            title='Valor da ação'
        ),
        showlegend=True
    )
    data = [real_data, rbf]
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/training')


# set_training()
predict_prices()

