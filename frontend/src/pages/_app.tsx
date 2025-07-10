import { AppProps } from 'next/app';
import { AuthProvider } from '@/hooks/useAuth';

export default function MyApp({ Component, pageProps }: AppProps) {
  return (
    <AuthProvider>
      <Component {...pageProps} />
    </AuthProvider>
  );
}
