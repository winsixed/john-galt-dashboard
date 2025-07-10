import { useState, useEffect } from 'react';
import axios from 'axios';

interface Props { onSubmit: any; initial?: any; }
export function UserForm({ onSubmit, initial }: Props) {
  const [username, setUsername] = useState(initial?.username || '');
  const [password, setPassword] = useState('');
  const [role, setRole] = useState(initial?.role_id || 1);
  const [roles, setRoles] = useState<{id:number,name:string}[]>([]);
  useEffect(() => { axios.get('/roles').then(r => setRoles(r.data)); }, []);
  return (
    <form onSubmit={e => { e.preventDefault(); onSubmit({ username, password, role_id: role }); }}>
      <input value={username} onChange={e=>setUsername(e.target.value)} placeholder="Username" required />
      <input type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="Password" required />
      <select value={role} onChange={e=>setRole(+e.target.value)}>
        {roles.map(r => <option key={r.id} value={r.id}>{r.name}</option>)}
      </select>
      <button type="submit" className="btn mt-2">Сохранить</button>
    </form>
  );
}
