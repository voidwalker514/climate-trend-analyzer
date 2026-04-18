from prophet import Prophet

def forecast_temperature(df):
    prophet_df = df[['date', 'temperature']]
    prophet_df.columns = ['ds', 'y']

    model = Prophet()
    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=365)
    forecast = model.predict(future)

    return model, forecast