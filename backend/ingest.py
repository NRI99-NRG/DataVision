import pandas as pd


csv_path = "backend/data/50_Startups.csv"
json_path = "backend/data/50_Startups.json"
xml_path = "backend/data/50_Startups.xml"
output_path = "backend/data/clean_data.csv"


df_csv = pd.read_csv(csv_path)


def clean_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("&", "and")
    )
    return df

df_csv = clean_columns(df_csv)

print("Columns after cleaning:", df_csv.columns.tolist())


df_json = pd.read_json(json_path)
df_json = clean_columns(df_json)


df_xml = pd.read_xml(xml_path)
df_xml = clean_columns(df_xml)


combined_df = pd.concat([df_csv, df_json, df_xml], ignore_index=True)


combined_df["ROI"] = combined_df.apply(
    lambda row: (row["Profit"] / row["RandD_Spend"] * 100) if row["RandD_Spend"] != 0 else None,
    axis=1
)


combined_df.to_csv(output_path, index=False)

print("Combined data shape:", combined_df.shape)
print("Cleaned unified data saved at:", output_path)
print("\nSample data:\n", combined_df.head())
