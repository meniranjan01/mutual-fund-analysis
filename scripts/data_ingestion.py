import pandas as pd
import os

path = "data/raw"

for file in os.listdir(path):

    if file.endswith(".csv"):

        print("\n" + "="*60)
        print(f"FILE: {file}")

        df = pd.read_csv(os.path.join(path, file))

        # Basic information
        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        # Missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Duplicate rows
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())