import React, { useState } from "react";
import Layout from "../../layouts/layout";
import Button from "../../components/button/button";
import Input from "../../components/input/inputFile/input";
import Hero from "../../components/hero/hero";
import Navbar from "../../components/navbar/navbar";
import "./homepage.css";
import axios from "axios";
import JSZip from "jszip";

const Homepage = () => {
  const [imagePath, setImagePath] = useState('');
  const [additionalData, setAdditionalData] = useState([]);

  const handleFileUpload = async (e) => {
    const file = e.target.files[0];
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('http://localhost:5000/api/process', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const result = await response.json();
      setImagePath(result.image_url);
      setAdditionalData(result.pred);
    } catch (error) {
      console.error('Error processing image:', error);
    }
  };

  return (
    <div>
      <h1>React App</h1>
      <input type="file" onChange={handleFileUpload} />
      {imagePath && (
        <div>
          <p>Prediction: {additionalData}</p>
          <img src={`http://localhost:5000/${imagePath}`} alt="Processed Image" />
        </div>
      )}
    </div>
  );
};

export default Homepage;