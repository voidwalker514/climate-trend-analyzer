import os

from src.data_loader import generate_climate_data
from src.preprocessing import preprocess
from src.anomaly_detection import detect_anomalies
from src.forecasting import forecast_temperature

def main():
    print("🚀 Starting Climate Trend Analyzer Pipeline...\n")

    # ✅ Ensure folders exist
    os.makedirs("data", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    # Step 1: Generate Data
    print("📊 Generating climate data...")
    df = generate_climate_data()

    # Step 2: Preprocess Data
    print("🧹 Cleaning and preprocessing data...")
    df = preprocess(df)

    # Step 3: Detect Anomalies
    print("⚠️ Detecting anomalies...")
    df = detect_anomalies(df)

    # Step 4: Forecasting
    print("🔮 Running forecasting model...")
    model, forecast = forecast_temperature(df)

    # Step 5: Save Outputs
    print("💾 Saving outputs...")

    df.to_csv("outputs/final_data.csv", index=False)
    forecast.to_csv("outputs/forecast.csv", index=False)

    print("\n✅ Pipeline completed successfully!")
    print("📁 Check 'outputs/' folder for results.")

if __name__ == "__main__":
    main()