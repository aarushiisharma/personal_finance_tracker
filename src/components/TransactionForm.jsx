import React, { useState } from "react";

export default function TransactionForm({ onAdd }) {
  const [category, setCategory] = useState("");
  const [amount, setAmount] = useState("");
  const [type, setType] = useState("expense");
  const [note, setNote] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    if (!category || !amount) return alert("Category and amount required");
    const payload = {
      category,
      amount: Number(amount),
      type,
      note,
      date: new Date().toISOString(),
    };
    await onAdd(payload);
    setCategory("");
    setAmount("");
    setNote("");
  }

  return (
    <form onSubmit={handleSubmit} style={{ marginTop: 12 }}>
      <div className="form-row">
        <input
          className="input"
          placeholder="Category (e.g., Salary, Uber)"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />
        <input
          className="input"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
      </div>
      <div className="form-row">
        <select
          className="input"
          value={type}
          onChange={(e) => setType(e.target.value)}
        >
          <option value="expense">Expense</option>
          <option value="income">Income</option>
        </select>
        <input
          className="input"
          placeholder="Short note"
          value={note}
          onChange={(e) => setNote(e.target.value)}
        />
      </div>
      <div style={{ textAlign: "right" }}>
        <button className="btn" type="submit">
          Add
        </button>
      </div>
    </form>
  );
}
