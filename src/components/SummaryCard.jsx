import React from "react";

export default function SummaryCard({ balance, income, expense }) {
  return (
    <div style={{ display: "flex", gap: 12, marginBottom: 12 }}>
      <div style={{ flex: 1 }} className="card">
        <div className="small">Balance</div>
        <div style={{ fontSize: 24, fontWeight: 700 }}>₹{balance}</div>
      </div>
      <div style={{ width: 140 }} className="card">
        <div className="small">Income</div>
        <div className="small income">₹{income}</div>
      </div>
      <div style={{ width: 140 }} className="card">
        <div className="small">Expense</div>
        <div className="small expense">₹{expense}</div>
      </div>
    </div>
  );
}
