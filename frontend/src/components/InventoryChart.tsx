import { LineChart, Line, XAxis, YAxis, Tooltip } from 'recharts';

export function InventoryChart({ data }) {
  return (
    <LineChart width={600} height={300} data={data}>
      <XAxis dataKey="timestamp" /><YAxis />
      <Tooltip />
      <Line type="monotone" dataKey="count" />
    </LineChart>
  );
}
