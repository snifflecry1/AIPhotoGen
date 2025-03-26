import React from "react";
import ReactDOM from "react-dom/client";
import Client from "./components/client";
import "./styles/global.css";


const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Client />
  </React.StrictMode>
);
