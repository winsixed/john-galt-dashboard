from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import app.db.models as models
from app.config import Settings

config = context.config
fileConfig(config.config_file_name)
target_metadata = models.Base.metadata

cfg = config.get_section(config.config_ini_section)
cfg["sqlalchemy.url"] = Settings().DATABASE_URL
engine = engine_from_config(cfg, prefix="sqlalchemy.", poolclass=pool.NullPool)

def run_migrations_offline():
    context.configure(url=cfg["sqlalchemy.url"], target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine
    with connectable.connect() as conn:
        context.configure(connection=conn, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
