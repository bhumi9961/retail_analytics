"""Example tests - these already pass. Use them as a pattern for your own."""

from retail.config import get_settings


def test_db_url_uses_pymysql_driver(monkeypatch):
    monkeypatch.setenv("DB_USER", "u")
    monkeypatch.setenv("DB_PASSWORD", "p")
    monkeypatch.setenv("DB_HOST", "h")
    monkeypatch.setenv("DB_PORT", "1234")
    monkeypatch.setenv("DB_NAME", "d")

    assert get_settings().db_url == "mysql+pymysql://u:p@h:1234/d"


def test_relative_paths_are_resolved_from_project_root(monkeypatch):
    monkeypatch.setenv("RAW_DIR", "data/raw")
    assert get_settings().raw_dir.is_absolute()
