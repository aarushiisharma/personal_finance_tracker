import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import TransactionForm from "../components/TransactionForm";
import TransactionList from "../components/TransactionList";
import SummaryCard from "../components/SummaryCard";
import {
  fetchTransactions,
  createTransaction,
  deleteTransaction,
} from "../api";

export default function Dashboard() {
  const [transactions, setTransactions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    load();
  }, []);

  async function load() {
    setLoading(true);
    try {
      const data = await fetchTransactions();
      setTransactions(data);
    } catch (e) {
      setError(e.message);
    }
    setLoading(false);
  }

  async function add(tx) {
    try {
      const created = await createTransaction(tx);
      setTransactions((prev) => [...prev, created]);
    } catch (e) {
      alert(e.message);
    }
  }

  async function remove(id) {
    if (!confirm("Delete this transaction?")) return;
    try {
      await deleteTransaction(id);
      setTransactions((prev) => prev.filter((t) => t.id !== id));
    } catch (e) {
      alert(e.message);
    }
  }

  const income = transactions
    .filter((t) => t.type === "income")
    .reduce((s, n) => s + Number(n.amount), 0);
  const expense = transactions
    .filter((t) => t.type === "expense")
    .reduce((s, n) => s + Number(n.amount), 0);
  const balance = income - expense;

  return (
    <>
      <Header />
      <div className="grid">
        <div>
          <div className="card">
            <SummaryCard balance={balance} income={income} expense={expense} />
            <TransactionForm onAdd={add} />
            <div className="tx-list">
              {loading && <div className="small">Loading...</div>}
              {error && <div className="small">Error: {error}</div>}
              {!loading && !error && (
                <TransactionList
                  transactions={transactions}
                  onDelete={remove}
                />
              )}
            </div>
          </div>
        </div>
        <div>
          <div className="card">
            <h3>Quick Insights</h3>
            <p className="small">Transactions: {transactions.length}</p>
            <p className="small">Income: ₹{income}</p>
            <p className="small">Expense: ₹{expense}</p>
            <p className="small">Balance: ₹{balance}</p>
          </div>
        </div>
      </div>
    </>
  );
}
