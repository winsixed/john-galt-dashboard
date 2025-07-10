import { useState, useEffect } from 'react';

export function useInventory() {
  const [data, setData] = useState([]);
  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws/inventory");
    ws.onmessage = e => setData(prev => [...prev, JSON.parse(e.data)]);
    return () => ws.close();
  }, []);
  return data;
}
