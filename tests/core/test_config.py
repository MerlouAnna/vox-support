import pytest
from pydantic import ValidationError

from vox.core.config import Settings


def test_settings_defaults_are_safe():
    settings = Settings(_env_file=None, environment="local")
    assert settings.environment == "local"
    assert settings.debug is False
    assert settings.log_level == "INFO"


def test_settings_rejects_unknown_environment():
    with pytest.raises(ValidationError):
        Settings(_env_file=None, environment="dev")


def test_env_overrides_default(monkeypatch):
    monkeypatch.setenv("VOX_LOG_LEVEL", "WARNING")
    settings = Settings(_env_file=None, environment="staging")
    assert settings.log_level == "WARNING"
