import { withAuth } from '@/lib/withAuth';
import { UserList } from '@/components/UserList';

function UsersPage() {
  return <UserList />;
}

export default withAuth(UsersPage);
