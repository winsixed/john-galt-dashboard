import React from 'react';
import { useQuery } from 'react-query';
import axios from 'axios';
import Link from 'next/link';

export function UserList() {
  const { data } = useQuery('users', () => axios.get('/users').then(r => r.data));
  return (
    <div>
      <Link href="/users/create"><button className="btn mb-4">Создать</button></Link>
      <table className="w-full">
        <thead><tr><th>ID</th><th>Username</th><th>Role</th><th>Действия</th></tr></thead>
        <tbody>
          {data?.map(u => (
            <tr key={u.id}>
              <td>{u.id}</td><td>{u.username}</td><td>{u.role_id}</td>
              <td><Link href={`/users/${u.id}/edit`}>Ред.</Link></td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
