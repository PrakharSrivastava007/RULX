import React, { useState } from "react";
import Layout from "../components/Layout";
import InputForm from "../components/InputForm";
import { predict } from "../services/api";
import { motion } from "framer-motion";

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
          <div style={{ display: "flex", gap: "20px", marginTop: "30px" }}>
  
      {[
        { title: "RUL", value: result.rul },
        { title: "Failure Risk", value: result.probability },
        { title: "Days Left", value: result.days_to_failure },
      ].map((item, i) => (
    
        <motion.div
          key={i}
          className="card"
          style={{ flex: 1 }}
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: i * 0.2 }}
        >
          <h3>{item.title}</h3>
          <p style={{ fontSize: "30px", fontWeight: "600" }}>
            {item.value}
          </p>
        </motion.div>
      ))}

    </div>

              {/* Status Indicator */}
              <motion.div
              initial={{ scale: 0.8, opacity: 0 }}
              animate={{ scale: 1, opacity: 1 }}
              style={{
                marginTop: "25px",
                padding: "15px",
                borderRadius: "20px",
                background: getColor(),
                color: "white",
                width: "220px",
                textAlign: "center",
                fontWeight: "600",
                boxShadow: "0 6px 20px rgba(0,0,0,0.1)"
      }}
    >
      {getStatus()}
    </motion.div>
        </>
      )}
    </Layout>
  );
};

export default Dashboard;