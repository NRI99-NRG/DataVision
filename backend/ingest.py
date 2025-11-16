import pandas as pd

# ✅ File paths
csv_path = "backend/data/50_Startups.csv"
json_path = "backend/data/50_Startups.json"
xml_path = "backend/data/50_Startups.xml"
output_path = "backend/data/clean_data.csv"

# 1️⃣ Read CSV
df_csv = pd.read_csv(csv_path)

# 2️⃣ Clean column names (replace spaces + special chars)
df_csv.columns = (
    df_csv.columns
    .str.strip()
    .str.replace(" ", "_")
    .str.replace("&", "and")
)
print("🔍 Columns after cleaning:", df_csv.columns.tolist())

# 3️⃣ Create and read JSON
df_csv.to_json(json_path, orient="records", indent=4)
df_json = pd.read_json(json_path)

# 4️⃣ Create and read XML
df_csv.to_xml(xml_path, index=False)
df_xml = pd.read_xml(xml_path)

# 5️⃣ Combine all sources
combined_df = pd.concat([df_csv, df_json, df_xml], ignore_index=True)

# 6️⃣ Add derived metric (✅ match actual column name)
combined_df["ROI"] = (combined_df["Profit"] / combined_df["RandD_Spend"]) * 100

# 7️⃣ Save unified cleaned data
combined_df.to_csv(output_path, index=False)

print("✅ Combined data shape:", combined_df.shape)
print("✅ Cleaned unified data saved at:", output_path)
print("\nSample data:\n", combined_df.head())
