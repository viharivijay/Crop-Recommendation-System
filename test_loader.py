from utils.data_loader import load_all_data

data = load_all_data()

print("\nDatasets Loaded:\n")

for name, df in data.items():
    print(f"{name} --> {df.shape}")