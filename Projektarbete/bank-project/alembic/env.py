import sys, os

# Importera bank-mappen i systemvägen, Importera Base från mina modeller
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from bank.models import Base

from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# Alembic-konfigurationsobjekt
config = context.config

# Läser in logging-konfiguration
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata för 'autogenerate'
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Kör migrationer i offline-läge."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Kör migrationer i online-läge."""
    
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

# Välj rätt funktion beroende på körläge
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online