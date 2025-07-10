import { withAuth } from '@/lib/withAuth';
import { UserForm } from '@/components/UserForm';
import { useMutation, useQueryClient } from 'react-query';
import axios from 'axios';

function CreateUser() {
  const qc = useQueryClient();
  const mutation = useMutation(
    (newUser) => axios.post('/users', newUser),
    {
      onSuccess: () => qc.invalidateQueries('users'),
    }
  );
  return <UserForm onSubmit={(data) => mutation.mutate(data)} />;
}

export default withAuth(CreateUser);
