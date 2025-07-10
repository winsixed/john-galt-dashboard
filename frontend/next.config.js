module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      { source: '/auth/:path*', destination: 'http://localhost:8000/auth/:path*' },
      { source: '/users/:path*', destination: 'http://localhost:8000/users/:path*' },
      { source: '/roles/:path*', destination: 'http://localhost:8000/roles/:path*' },
      { source: '/ws/:path*', destination: 'ws://localhost:8000/ws/:path*' }
    ];  
  }
};
