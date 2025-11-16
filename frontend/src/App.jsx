import { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, Legend, ResponsiveContainer } from "recharts";
import "./App.css";

function App() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch data from FastAPI
    fetch("http://127.0.0.1:8000/summary")
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
      .catch((err) => {
        console.error("Error fetching data:", err);
        setLoading(false);
      });
  }, []);

  if (loading) return <h2 style={{ textAlign: "center", marginTop: "50px" }}>Loading...</h2>;
  if (!data) return <h2 style={{ textAlign: "center", marginTop: "50px" }}>No data available</h2>;

  // Prepare chart data
  const chartData = Object.keys(data.spend_by_state.RandD_Spend).map((state) => ({
    state,
    RandD_Spend: data.spend_by_state.RandD_Spend[state],
    Marketing_Spend: data.spend_by_state.Marketing_Spend[state],
  }));

  return (
    <div className="dashboard">
      <h1> DataVision Dashboard</h1>

      <div className="cards">
        <div className="card">
          <h3>Total Profit</h3>
          <p>${data.total_profit.toLocaleString()}</p>
        </div>
        <div className="card">
          <h3>Average Profit</h3>
          <p>${data.average_profit.toFixed(2)}</p>
        </div>
        <div className="card">
          <h3>Average ROI</h3>
          <p>{data.average_roi.toFixed(2)}%</p>
        </div>
        <div className="card">
          <h3>Records</h3>
          <p>{data.record_count}</p>
        </div>
      </div>

      <div className="chart-container">
        <h2> Spending by State</h2>
        <ResponsiveContainer width="100%" height={400}>
          <BarChart data={chartData}>
            <XAxis dataKey="state" />
            <YAxis />
            <Tooltip />
            <Legend />
            <Bar dataKey="RandD_Spend" fill="#8884d8" />
            <Bar dataKey="Marketing_Spend" fill="#82ca9d" />
          </BarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}

export default App;
