import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import React from "react";
import Homepage from "./pages/Homepage";
import Login from "./pages/Login";
import Player from "./pages/Player";
import "./index.scss";

export default function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Homepage />} />
                <Route path="login" element={<Login />} />
                <Route path="player" element={<Player />} />
            </Routes>
        </BrowserRouter>
    );
}

const root = ReactDOM.createRoot(document.getElementById("root")!);
root.render(<App />);
