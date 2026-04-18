def detect_anomalies(df):
    mean = df['temperature'].mean()
    std = df['temperature'].std()

    df['z_score'] = (df['temperature'] - mean) / std
    df['anomaly'] = df['z_score'].apply(lambda x: 1 if abs(x) > 2 else 0)

    return df