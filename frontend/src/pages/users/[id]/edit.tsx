import { withAuth } from '@/lib/withAuth';
import { UserForm } from '@/components/UserForm';
import { useMutation, useQuery, useQueryClient } from 'react-query';
import axios from 'axios';
import { useRouter } from 'next/router';

function EditUser() {
  const { query } = useRouter();
  const id = query.id as string;
  const qc = useQueryClient();
  const { data } = useQuery(['user', id], () => axios.get(`/users/${id}`).then(r => r.data));
  const mutation = useMutation(
    (updated) => axios.put(`/users/${id}`, updated),
    { onSuccess: () => qc.invalidateQueries('users') }
  );
  if (!data) return <div>Loading...</div>;
  return <UserForm initial={data} onSubmit={(d) => mutation.mutate(d)} />;
}

export default withAuth(EditUser);
