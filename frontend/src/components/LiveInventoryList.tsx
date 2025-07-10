export function LiveInventoryList({ data }) {
  return (
    <ul>
      {data.map((item, i) => (
        <li key={i}>{item.name}: {item.count}</li>
      ))}
    </ul>
  );
}
