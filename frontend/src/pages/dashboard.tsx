import { withAuth } from '@/lib/withAuth';
import { useInventory } from '@/hooks/useInventory';
import { LiveInventoryList } from '@/components/LiveInventoryList';
import { InventoryChart } from '@/components/InventoryChart';

function Dashboard() {
  const data = useInventory();
  return (
    <div className="p-4">
      <h1 className="text-2xl mb-4">Inventory Dashboard</h1>
      <LiveInventoryList data={data} />
      <InventoryChart data={data} />
    </div>
  );
}

export default withAuth(Dashboard);
