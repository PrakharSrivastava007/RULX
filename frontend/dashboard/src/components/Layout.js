import React from "react";
import { FaChartLine, FaFileAlt } from "react-icons/fa";
const Layout = ({ children }) => {
  return (
    <div style={{
  width: "240px",
  background: "linear-gradient(180deg, #f3e9e2, #efe1d8)",
  padding: "25px",
  borderRight: "1px solid #e6d5c9"
}}>
  <h2 style={{ color: "#c97c5d" }}>RULX</h2>
  <p style={{ fontSize: "13px", color: "#7a7a7a" }}>
    AI Predictive Suite
  </p>

  <div style={{ marginTop: "40px" }}>
    <p><FaChartLine /> Dashboard</p>
    <p><FaChartLine /> Analytics</p>
    <p><FaFileAlt /> Reports</p>
  </div>
</div>
  );
};

export default Layout;