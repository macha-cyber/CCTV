"use client";

import { useEffect } from "react";

export default function Page() {

  useEffect(() => {

    const ws = new WebSocket("ws://localhost:8000/ws");

    ws.onmessage = (msg) => {

      const data = JSON.parse(msg.data);

      if (data.type === "person_detected") {

        const audio = new Audio("/chime.mp3");
        audio.play();

        alert("人を検知しました");
      }
    };

    return () => ws.close();

  }, []);

  return (
    <main style={{ padding: 40 }}>
      <h1>Camera Monitor</h1>
      <p>WebSocket Listening...</p>
    </main>
  );
}