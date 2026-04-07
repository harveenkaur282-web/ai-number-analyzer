import { useState } from "react";

const API = import.meta.env.VITE_API_URL || "http://localhost:8000";

export default function App() {
  const [number, setNumber] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [logs, setLogs] = useState([]);

  async function analyze() {
    if (!number) return;
    setLoading(true);
    setResult(null);
    setLogs(["Initiating globally distributed analysis..."]);
    const res = await fetch(`${API}/analyze/${number}`);
    const data = await res.json();
    // Stream logs one by one for that hacker feel
    for (let i = 0; i < data.logs.length; i++) {
      await new Promise(r => setTimeout(r, 120));
      setLogs(prev => [...prev, data.logs[i]]);
    }
    setResult(data);
    setLoading(false);
  }

  return (
    <div style={{ maxWidth: 720, margin: "0 auto", padding: "2rem", fontFamily: "monospace" }}>
      <h1 style={{ fontSize: 22, marginBottom: 8 }}>
        🌐 Number Analyzer 9000™
      </h1>
      <p style={{ fontSize: 13, color: "#888", marginBottom: 24 }}>
        Enterprise-grade distributed AI system for determining if a number is even.
      </p>

      <div style={{ display: "flex", gap: 8, marginBottom: 24 }}>
        <input
          type="number"
          value={number}
          onChange={e => setNumber(e.target.value)}
          placeholder="Enter a number..."
          style={{ flex: 1, padding: "8px 12px", fontSize: 16, border: "1px solid #ccc", borderRadius: 8 }}
        />
        <button onClick={analyze} disabled={loading} style={{ padding: "8px 20px", borderRadius: 8, cursor: "pointer" }}>
          {loading ? "Analyzing..." : "Analyze ↗"}
        </button>
      </div>

      {/* Terminal log */}
      <div style={{
        background: "#0d0d0d", color: "#00ff41", fontFamily: "monospace",
        fontSize: 12, padding: 16, borderRadius: 8, minHeight: 160,
        maxHeight: 300, overflowY: "auto", marginBottom: 20
      }}>
        {logs.map((log, i) => <div key={i}>{`> ${log}`}</div>)}
        {loading && <div style={{ opacity: 0.6 }}>█</div>}
      </div>

      {/* Result card */}
      {result && (
        <div style={{ border: "1px solid #ddd", borderRadius: 12, padding: 20 }}>
          <div style={{ display: "flex", gap: 12, marginBottom: 16 }}>
            <Badge label="Even" value={result.even ? "YES" : "NO"} color={result.even ? "green" : "red"} />
            <Badge label="Prime" value={result.prime ? "YES" : "NO"} color={result.prime ? "blue" : "gray"} />
            <Badge label="Status" value={result.status.toUpperCase()} color="purple" />
          </div>
          <p style={{ fontSize: 13 }}><b>ML says:</b> {result.ml_prediction}</p>
          <p style={{ fontSize: 13 }}><b>Multiverse:</b> {result.multiverse_decision}</p>
          <p style={{ fontSize: 13 }}><b>Confidence:</b> {(result.confidence * 100).toFixed(1)}%</p>
          <p style={{ fontSize: 13 }}><b>Social:</b> {result.social_analysis}</p>
          <p style={{ fontSize: 13 }}><b>Academic:</b> {result.exam_result}</p>
          <div style={{ marginTop: 12, padding: 12, background: "#f5f5f5", borderRadius: 8, fontSize: 13 }}>
            🎭 {result.meme_output}
          </div>
        </div>
      )}
    </div>
  );
}

function Badge({ label, value, color }) {
  const colors = { green: "#16a34a", red: "#dc2626", blue: "#2563eb", gray: "#6b7280", purple: "#7c3aed" };
  return (
    <div style={{ textAlign: "center" }}>
      <div style={{ fontSize: 11, color: "#888" }}>{label}</div>
      <div style={{ fontWeight: 600, color: colors[color] }}>{value}</div>
    </div>
  );
}