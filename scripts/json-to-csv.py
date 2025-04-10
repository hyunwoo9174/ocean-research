from pathlib import Path
import pandas as pd

def json_to_csv(json_file, csv_file):
    df = pd.read_json(json_file)
    items = df["body"]["item"]
    df_items = pd.json_normalize(items)
    df_items.to_csv(csv_file, index=False)
    return print(f"Converted {json_file} to {csv_file}")

if __name__ == "__main__":
    DATA_DIR = Path.cwd() / "data"
    for year in range(1961, 2025):
        json_file = f"sooList_{year}.json"
        csv_file = f"sooList_{year}.csv"
        json_to_csv(DATA_DIR / json_file, DATA_DIR / csv_file)
    for element in ["E", "W", "S", "EC"]:
        json_file = f"sooCode_{element}.json"
        csv_file = f"sooCode_{element}.csv"
        json_to_csv(DATA_DIR / json_file, DATA_DIR / csv_file)
    print("All json files converted to csv files.")
