from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": " DataVision API is running!"}

@app.get("/summary")
def get_summary():
    df = pd.read_csv("backend/data/clean_data.csv")

    # Replace inf or NaN with 0 to make data JSON-safe
    df.replace([float('inf'), float('-inf')], pd.NA, inplace=True)
    df.fillna(0, inplace=True)

    total_profit = df["Profit"].sum()
    avg_profit = df["Profit"].mean()
    avg_roi = df["ROI"].mean()
    spend_by_state = (
        df.groupby("State")[["RandD_Spend", "Marketing_Spend"]]
        .sum()
        .fillna(0)
        .to_dict()
    )

    return {
        "total_profit": round(total_profit, 2),
        "average_profit": round(avg_profit, 2),
        "average_roi": round(avg_roi, 2),
        "record_count": len(df),
        "spend_by_state": spend_by_state,
    }
