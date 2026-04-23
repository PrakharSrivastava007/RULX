import React, { useState } from "react";

const InputForm = ({ onSubmit }) => {
  const [form, setForm] = useState({
    setting1: 0,
    setting2: 0,
    sensor1: 0,
    sensor2: 0,
    sensor3: 0,
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: parseFloat(e.target.value) });
  };

  const handleSubmit = () => {
    onSubmit(form);
  };

  return (
    <div className="card" style={{ marginTop: "20px" }}>
      <h3>Enter Machine Data</h3>

      {Object.keys(form).map((key) => (
        <div key={key} style={{ marginBottom: "10px" }}>
          <label>{key}</label>
          <input
            type="number"
            name={key}
            value={form[key]}
            onChange={handleChange}
            style={{ marginLeft: "10px", padding: "5px" }}
          />
        </div>
      ))}

      <button onClick={handleSubmit}>Predict</button>
    </div>
  );
};

export default InputForm;