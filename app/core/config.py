

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):


    # Application Settings
    app_name: str
    app_env: str

    # Database Settings
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: int

    # Redis Settings
    redis_host: str
    redis_port: int
    redis_db : int
    redis_url: str



    # Kafka Settings
    kafka_bootstrap_servers: str

    # JWT Settings
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    # Other Settings
    debug: bool = False

    model_config = SettingsConfigDict(env_file="abcem/.env", extra="ignore")

    @field_validator("redis_url", mode="after")
    def assemble_redis_url(cls, value, values):
        """
        Constructs REDIS_URL from individual components if not provided.
        """
        if not value:
            host = values.get("REDIS_HOST", "localhost")
            port = values.get("REDIS_PORT", 6379)
            db = values.get("REDIS_DB", 0)


            # if password:
            #     return f"redis://:{password}@{host}:{port}/{db}"
            return f"redis://{host}:{port}/{db}"
        return value

# Instantiate settings
settings = Settings()
