import pandas as pd
import numpy as np
import os

def generate_climate_data(days=365*5):
    # ✅ Get project root path
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # ✅ Create data folder safely
    data_path = os.path.join(BASE_DIR, 'data')
    os.makedirs(data_path, exist_ok=True)

    file_path = os.path.join(data_path, 'climate_data.csv')

    # Generate data
    dates = pd.date_range(start="2018-01-01", periods=days)

    temp = 25 + 10*np.sin(np.linspace(0, 20, days)) + np.random.normal(0, 2, days)
    rainfall = np.abs(np.random.normal(5, 2, days))
    humidity = np.random.uniform(40, 90, days)

    anomaly_indices = np.random.choice(days, 20)
    temp[anomaly_indices] += np.random.uniform(10, 15, 20)

    df = pd.DataFrame({
        "date": dates,
        "temperature": temp,
        "rainfall": rainfall,
        "humidity": humidity
    })

    # ✅ Save file safely
    df.to_csv(file_path, index=False)

    return df