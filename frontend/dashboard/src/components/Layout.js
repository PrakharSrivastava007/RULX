import React from "react";

const Layout = ({ children }) => {
  return (
    <div style={{ display: "flex", minHeight: "100vh" }}>
      
      {/* Sidebar */}
      <div style={{
        width: "220px",
        background: "#f3e9e2",
        padding: "20px",
        borderRight: "1px solid #e6d5c9"
      }}>
        <h2 style={{ color: "#c97c5d" }}>RULX</h2>
        <p style={{ color: "#7a7a7a", fontSize: "14px" }}>
          Predictive Intelligence
        </p>

        <div style={{ marginTop: "40px" }}>
          <p>📊 Dashboard</p>
          <p>📈 Analytics</p>
          <p>📄 Reports</p>
        </div>
      </div>

      {/* Main */}
      <div style={{ flex: 1, padding: "30px" }}>
        {children}
      </div>
    </div>
  );
};

export default Layout;