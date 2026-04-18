import plotly.express as px

def plot_temperature(df):
    fig = px.line(df, x='date', y='temperature', title='Temperature Trend')
    return fig

def plot_anomalies(df):
    fig = px.scatter(df, x='date', y='temperature', color='anomaly',
                     title='Anomaly Detection')
    return fig