import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { useRouter } from 'next/router';

interface AuthContext { token: string | null; login: (t: string, r: string) => void; logout(): void; }
const AuthContext = createContext<AuthContext>(null!);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [token, setToken] = useState<string | null>(null);
  const router = useRouter();
  useEffect(() => { const t = localStorage.getItem('access'); if (t) setToken(t); }, []);
  const login = (access: string, refresh: string) => {
    localStorage.setItem('access', access);
    localStorage.setItem('refresh', refresh);
    setToken(access);
    router.push('/dashboard');
  };
  const logout = () => { localStorage.clear(); setToken(null); router.push('/login'); };
  return <AuthContext.Provider value={{ token, login, logout }}>{children}</AuthContext.Provider>;
};

export const useAuth = () => useContext(AuthContext);
