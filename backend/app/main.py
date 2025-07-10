from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from prometheus_fastapi_instrumentator import Instrumentator
from loguru import logger

from app.config import Settings
from app.db.session import engine
from app.db import models
from app.auth.routes import router as auth_router
from app.routers.users import router as users_router
from app.routers.roles import router as roles_router
from app.routers.ws import router as ws_router

settings = Settings()

# Loguru
logger.add("logs/app_{time:YYYY-MM-DD}.log", rotation="10 MB", retention="7 days", serialize=True)
logger.info("Starting John Galt Dashboard API")

# Rate Limiter
limiter = Limiter(key_func=get_remote_address, default_limits=[settings.RATE_LIMIT])

app = FastAPI(title="John Galt Dashboard")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rate limiter registration
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
@app.middleware("http")
async def add_rate_limit(request: Request, call_next):
    response = await limiter(request, call_next)
    return response

# Prometheus
Instrumentator().instrument(app).expose(app, include_in_schema=False, endpoint="/metrics")

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/auth")
app.include_router(users_router, prefix="/users")
app.include_router(roles_router, prefix="/roles")
app.include_router(ws_router)
