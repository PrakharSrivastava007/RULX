import React, { useState } from "react";
import Layout from "../components/Layout";
import InputForm from "../components/InputForm";
import { predict } from "../services/api";

const Dashboard = () => {
  const [result, setResult] = useState(null);

  const handlePredict = async (formData) => {
    const features = Array(66).fill(0);

    features[0] = formData.setting1;
    features[1] = formData.setting2;
    features[2] = formData.sensor1;

    const sequence = Array(30).fill(features);

    const res = await predict({ sequence });
    setResult(res.data);
  };

  const getStatus = () => {
    if (!result) return "";
    if (result.probability > 0.6) return "Critical";
    if (result.probability > 0.3) return "Warning";
    return "Healthy";
  };

  const getColor = () => {
    if (!result) return "#ccc";
    if (result.probability > 0.6) return "#e07a5f";
    if (result.probability > 0.3) return "#f2cc8f";
    return "#81b29a";
  };

  return (
    <Layout>
      <h1 style={{ marginBottom: "20px" }}>Machine Health Dashboard</h1>

      {/* Input Form */}
      <InputForm onSubmit={handlePredict} />

      {/* Result Section */}
      {result && (
        <>
          <div style={{ marginTop: "30px", display: "flex", gap: "20px" }}>
            
            {/* RUL Card */}
            <div className="card" style={{ flex: 1 }}>
              <h3>RUL</h3>
              <p style={{ fontSize: "28px" }}>{result.rul}</p>
            </div>

            {/* Probability */}
            <div className="card" style={{ flex: 1 }}>
              <h3>Failure Risk</h3>
              <p style={{ fontSize: "28px" }}>{result.probability}</p>
            </div>

            {/* Days */}
            <div className="card" style={{ flex: 1 }}>
              <h3>Days Left</h3>
              <p style={{ fontSize: "28px" }}>{result.days_to_failure}</p>
            </div>
          </div>

          {/* Status Indicator */}
          <div
            style={{
              marginTop: "20px",
              padding: "15px",
              borderRadius: "12px",
              background: getColor(),
              color: "white",
              width: "200px",
              textAlign: "center",
              fontWeight: "bold"
            }}
          >
            {getStatus()}
          </div>
        </>
      )}
    </Layout>
  );
};

export default Dashboard;