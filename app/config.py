import os
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

if os.getenv("CQLENG_ALLOW_SCHEMA_MANAGEMENT") is None:
    os.environ["CQLENG_ALLOW_SCHEMA_MANAGEMENT"] = "1"

class Settings(BaseSettings):
    proj_name: str = Field(..., env='PROJ_NAME')
    astra_db_client_id: str = Field(..., env='ASTRA_DB_CLIENT_ID')
    astra_db_client_secret: str = Field(..., env='ASTRA_DB_CLIENT_SECRET')
    redis_url: str = Field(..., env='REDIS_URL')

    model_config = SettingsConfigDict(env_file=".env", extra="allow")



@lru_cache
def get_settings():
    return Settings()