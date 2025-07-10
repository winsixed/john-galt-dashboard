# John Galt Dashboard

Монорепозиторий с FastAPI + Next.js, PostgreSQL 17 (SSL), Redis, WebSocket, Telegram-ботом.

## Структура
- `backend/` — FastAPI, Alembic, Bot  
- `frontend/` — Next.js, React Query, Recharts  
- `docker-compose.yml` — локальный запуск (без БД, используем remote)  
- `nginx.conf`, `ecosystem.config.js` — продакшн

## Разработка
1. Скопировать `.env.example` → `.env`, заполнить  
2. `docker-compose up --build`  
3. Backend: `http://localhost:8000/docs`, Frontend: `http://localhost:3000`

## Безопасность
- CORS только для доверенных доменов (env `BACKEND_CORS_ORIGINS`)  
- Rate limit: env `RATE_LIMIT`  
- JWT, SSL-Postgres, Loguru (структурированные логи)

## CI/CD
- GitHub Actions: линт, тесты, миграции, coverage, деплой по SSH  
- Метрики Prometheus: `GET /metrics`

## Деплой
1. На VPS Ubuntu 22.04 установить Docker, Docker-Compose, Nginx, PM2  
2. Скопировать проект, настроить `nginx.conf`, `ecosystem.config.js`  
3. `pm2 start ecosystem.config.js`, `certbot --nginx`  
