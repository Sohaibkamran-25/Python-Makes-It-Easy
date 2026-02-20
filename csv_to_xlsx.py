import pandas as pd
import math
import os

# Path to your CSV file
csv_path = r"C:\Users\...\FILE_NAME.csv"
output_path = r"C:\Users\...\FILE_NAME.xlsx"

# Read CSV
df = pd.read_csv(csv_path)

# Excel row limit
rows_per_sheet = 1048575

# Write into multiple sheets
with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
    for i in range(math.ceil(len(df) / rows_per_sheet)):
        start = i * rows_per_sheet
        end = start + rows_per_sheet
        df.iloc[start:end].to_excel(writer, sheet_name=f"Part_{i+1}", index=False)

print(f"File is converted from csv to xlsx: {output_path}")
