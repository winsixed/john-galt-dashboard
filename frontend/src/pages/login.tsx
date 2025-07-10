import { useState } from 'react';
import axios from 'axios';
import { useAuth } from '@/hooks/useAuth';

export default function LoginPage() {
  const { login } = useAuth();
  const [u, setU] = useState(''); const [p, setP] = useState('');
  const submit = async () => {
    const { data } = await axios.post('/auth/login', { username: u, password: p });
    login(data.access_token, data.refresh_token);
  };
  return (
    <div className="p-4 max-w-sm mx-auto">
      <h1 className="text-xl mb-4">Вход</h1>
      <input placeholder="Username" value={u} onChange={e => setU(e.target.value)} className="w-full mb-2" />
      <input type="password" placeholder="Password" value={p} onChange={e => setP(e.target.value)} className="w-full mb-4" />
      <button onClick={submit} className="btn">Войти</button>
    </div>
}
