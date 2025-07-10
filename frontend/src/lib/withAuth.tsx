import { useAuth } from '@/hooks/useAuth';
import { useEffect } from 'react';
import { useRouter } from 'next/router';

export function withAuth(Component) {
  return props => {
    const { token } = useAuth();
    const router = useRouter();
    useEffect(() => { if (!token) router.push('/login'); }, [token]);
    return token ? <Component {...props} /> : null;
  };
}
