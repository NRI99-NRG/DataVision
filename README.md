# 📊 DataVision – Business Analytics Dashboard

A clean, interactive, end-to-end data analytics dashboard built using **FastAPI (backend)** and **React + Recharts (frontend)**.  
It demonstrates real-world data ingestion, transformation, API exposure, and insight visualization.

---

## ✅ Problem Statement
Business data is often stored in **different formats (CSV, JSON, XML)** making it difficult to clean, unify, analyze, and visualize for decision-making.  
This project solves the challenge by consolidating multi-format datasets into a single processed dataset and presenting meaningful insights through a dashboard.

---

## ✅ What Question Does This Project Answer?
**How can fragmented startup financial data from CSV, JSON, and XML sources be cleaned, unified, enriched with ROI metrics, exposed via an API, and visualized to support business decisions?**

---

## ✅ Project Summary
DataVision is a complete full-stack data pipeline where:

### 🔹 Backend (FastAPI + Pandas)
- Reads data from **three different datasets**:
  - `50_Startups.csv`
  - `50_Startups.json`
  - `50_Startups.xml`
- Cleans and standardizes column names
- Merges all sources into a **unified dataset**
- Calculates **ROI (Return on Investment)**
- Saves processed dataset as `clean_data.csv`
- Exposes data and summary metrics through REST API endpoints

### 🔹 Frontend (React + Recharts)
- Fetches data from FastAPI backend
- Displays insights in an elegant interactive dashboard

This project demonstrates your ability to handle:

✅ Data ingestion  
✅ Data cleaning & transformation  
✅ API development  
✅ Frontend visualization  
✅ Backend ↔ Frontend integration  

---

## 🧰 Tech Stack

### 🔻 Backend – FastAPI
- Python
- FastAPI
- Pandas
- Uvicorn
- CORS

### 🔻 Frontend – React
- React + Vite
- Recharts
- Modern CSS

---

## 📈 Dashboard Features

### ✅ Summary Cards
- **Total Profit**
- **Average Profit**
- **Average ROI**
- **Number of Records**

### ✅ Bar Chart – Spending by State
Compares:
- R&D Spend
- Marketing Spend  
for:
- California  
- Florida  
- New York  

---

## 🗂 Data Sources
This project uses **three independently stored datasets** representing business startup investments and performance:

| Format | File |
|--------|------|
| CSV | `50_Startups.csv` |
| JSON | `50_Startups.json` |
| XML | `50_Startups.xml` |

These are combined and transformed into:

✅ `clean_data.csv` (final unified dataset)

---

## 🚀 How to Run the Project

### 1️⃣ Start Backend
```
cd backend
uvicorn app:app --reload
```

### 2️⃣ Start Frontend
```
cd frontend
npm install
npm run dev
```

---

## ✅ Learning Outcomes
By completing DataVision, you demonstrate:

✅ multi-format data ingestion  
✅ cleaning & schema normalization  
✅ feature engineering (ROI)  
✅ API design and JSON responses  
✅ frontend data visualization  
✅ full-stack integration workflow  

---

## 📝 Optional Enhancements (Future Work)
✅ filtering by state  
✅ downloadable reports  
✅ authentication  
✅ more chart types  

---

## 📌 Repository
https://github.com/NRI99-NRG/DataVision
