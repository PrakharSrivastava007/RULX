import React from "react";

const ResultCard = ({ title, value }) => {
  return (
    <div className="card" style={{ width: "200px", textAlign: "center" }}>
      <h3 style={{ marginBottom: "10px" }}>{title}</h3>
      <p style={{ fontSize: "24px", fontWeight: "bold" }}>{value}</p>
    </div>
  );
};

export default ResultCard;