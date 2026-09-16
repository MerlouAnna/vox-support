from functools import lru_cache  # decorator to cache the result of a function call
from typing import Literal

from pydantic_settings import (
    # BaseSettings is a BaseModel that has the capability
    # to read settings from environment variables and other sources
    BaseSettings,
    SettingsConfigDict,  # configuration class for Pydantic settings models
)


class Settings(BaseSettings):
    environment: Literal["local", "staging", "production"] = "local"
    debug: bool = False
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",  # the path to the environment file containing the settings
        env_prefix="VOX_",  # the prefix for env variables related to the settings
        extra="forbid",  # forbid extra fields not defined in the settings model
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
