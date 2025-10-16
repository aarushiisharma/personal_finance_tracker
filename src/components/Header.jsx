import React from "react";

export default function Header() {
  return (
    <div className="header">
      <div className="brand">
        <div className="logo">PF</div>
        <div>
          <div style={{ fontWeight: 700 }}>Personal Finance</div>
          <div className="small">Track income & expense easily</div>
        </div>
      </div>
      <div>
        <button className="btn" onClick={() => location.reload()}>
          Refresh
        </button>
      </div>
    </div>
  );
}
