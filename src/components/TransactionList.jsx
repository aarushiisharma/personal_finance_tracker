import React from "react";

export default function TransactionList({ transactions, onDelete }) {
  if (!transactions.length)
    return <div className="small">No transactions yet — add one!</div>;

  return (
    <div>
      {transactions.map((tx) => (
        <div key={tx.id || tx._id} className="tx-item">
          <div>
            <div style={{ fontWeight: 700 }}>{tx.title}</div>
            <div className="small">{new Date(tx.date).toLocaleString()}</div>
          </div>
          <div style={{ textAlign: "right" }}>
            <div className={tx.type === "income" ? "income" : "expense"}>
              ₹{tx.amount}
            </div>
            <div style={{ marginTop: 8 }}>
              <button
                className="small"
                style={{ marginRight: 8 }}
                onClick={() => navigator.clipboard.writeText(tx.title)}
              >
                Copy
              </button>
              <button className="small" onClick={() => onDelete(tx.id || tx._id)}>
                Delete
              </button>
            </div>
          </div>
        </div>
      ))}
    </div>
  );
}
