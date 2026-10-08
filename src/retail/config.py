"""Project settings, read from environment variables / the .env file.

Nothing secret is hard-coded here. Copy .env.example to .env and edit it.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")


@dataclass(frozen=True)
class Settings:
    raw_dir: Path
    clean_dir: Path
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    log_level: str

    @property
    def db_url(self) -> str:
        """SQLAlchemy connection URL for MySQL (via the PyMySQL driver)."""
        return (
            f"mysql+pymysql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )


def get_settings() -> Settings:
    def path(var: str, default: str) -> Path:
        p = Path(os.getenv(var, default))
        return p if p.is_absolute() else PROJECT_ROOT / p

    return Settings(
        raw_dir=path("RAW_DIR", "data/raw"),
        clean_dir=path("CLEAN_DIR", "data/cleaned"),
        db_host=os.getenv("DB_HOST", "127.0.0.1"),
        db_port=int(os.getenv("DB_PORT", "3306")),
        db_name=os.getenv("DB_NAME", "retail_db"),
        db_user=os.getenv("DB_USER", "retail_user"),
        db_password=os.getenv("DB_PASSWORD", ""),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
    )
