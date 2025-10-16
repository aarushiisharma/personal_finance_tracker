export const BASE = "http://localhost:8000";

export async function fetchTransactions() {
  const res = await fetch(`${BASE}/transactions`);
  if (!res.ok) throw new Error("Failed to fetch transactions");
  return res.json();
}

export async function createTransaction(payload) {
  const res = await fetch(`${BASE}/transactions`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error("Failed to create transaction");
  return res.json();
}

export async function deleteTransaction(id) {
  const res = await fetch(`${BASE}/transactions/${id}`, { method: "DELETE" });
  if (!res.ok) throw new Error("Failed to delete transaction");
  return res.json();
}
