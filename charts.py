import plotly.graph_objs as go
from plotly.offline import plot
from data import get_dataset


def chart_variation():
    ds = get_dataset()
    x = ds.date
    y = ds.close

    data = [go.Scatter(x=x, y=y)]
    layout = go.Layout(
        xaxis=dict(
            # range=['11-07-2018', '11-10-2018'],
            title='Data'
        ),
        yaxis=dict(
            range=[min(x), max(y)],
            title='Valor da ação'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/Chartchart_variation')


def chart_candleticks(days=50):
    ds = get_dataset()
    ds_filter = ds.head(days)

    data = [go.Candlestick(
        x=ds_filter.date,
        open=ds_filter.open,
        high=ds_filter.high,
        low=ds_filter.low,
        close=ds_filter.close,
    )]

    layout = go.Layout(
        xaxis=dict(
            title='Data',
            rangeslider=dict(
                visible=False
            )
        ),
        yaxis=dict(
            title='Variação da ação'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/chart_candlestick')


def chart_price_variation():
    ds = get_dataset()
    ds['variation'] = ds['close'].sub(ds['open'])
    x = ds.date
    y = ds.variation

    data = [go.Bar(x=x, y=y)]
    layout = go.Layout(
        xaxis=dict(
            title='Data'
        ),
        yaxis=dict(
            title='Variação da ação'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/chart_price_variation')


def chart_correlation_open_close(days=50):
    ds = get_dataset()
    x = ds.open[:days]
    y = ds.close[:days]

    data = [go.Scatter(x=x, y=y, mode='markers')]
    layout = go.Layout(
        xaxis=dict(
            title='Preço de abertura'
        ),
        yaxis=dict(
            range=[x, y],
            title='Preço de fechamento'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/correlation_open_close')


def chart_correlation_high_close(days=50):
    ds = get_dataset()
    x = ds.high[:days]
    y = ds.close[:days]

    data = [go.Scatter(x=x, y=y, mode='markers')]
    layout = go.Layout(
        xaxis=dict(
            title='Preço de máxima'
        ),
        yaxis=dict(
            range=[x, y],
            title='Preço de fechamento'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/correlation_high_close')


def chart_correlation_low_close(days=50):
    ds = get_dataset()
    x = ds.low[:days]
    y = ds.close[:days]

    data = [go.Scatter(x=x, y=y, mode='markers')]
    layout = go.Layout(
        xaxis=dict(
            title='Preço de mínima'
        ),
        yaxis=dict(
            range=[x, y],
            title='Preço de fechamento'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/correlation_low_close')


def chart_correlation_volume_close(days=50):
    ds = get_dataset()
    x = ds.volume[:days]
    y = ds.close[:days]

    data = [go.Scatter(x=x, y=y, mode='markers')]
    layout = go.Layout(
        xaxis=dict(
            title='Volume'
        ),
        yaxis=dict(
            range=[x, y],
            title='Preço de fechamento'
        )
    )
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Charts_tmp/correlation_volume_close')


# Charts
chart_variation()
# chart_candleticks(50)
# chart_price_variation()
# chart_correlation_open_close()
# chart_correlation_high_close()
# chart_correlation_low_close()
# chart_correlation_volume_close()
