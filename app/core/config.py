from pydantic import BaseModel, Field, model_validator
import os


class Settings(BaseModel):
    # Application Settings
    # APP_NAME: str = Field(...)
    # APP_ENV: str = Field(...)

    # Database Settings
    POSTGRES_USER: str = Field("postgres")
    POSTGRES_PASSWORD: str = Field("afshin1994")
    POSTGRES_DB: str = Field("abcem_database")
    POSTGRES_HOST: str = Field("localhost")
    POSTGRES_PORT: int = Field(5432)
    DATABASE_URL: str = Field(f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}")


    # # Redis Settings
    # REDIS_HOST: str = Field(...)
    # REDIS_PORT: int = Field(...)
    # REDIS_DB: int = Field(...)
    # REDIS_PASSWORD: str = Field(None)  # Optional
    # REDIS_URL: str = Field(None)
    #
    # # Kafka Settings
    # KAFKA_BOOTSTRAP_SERVERS: str = Field(...)
    #
    # # JWT Settings
    # SECRET_KEY: str = Field(...)
    # ALGORITHM: str = Field(...)
    # ACCESS_TOKEN_EXPIRE_MINUTES: int = Field(...)
    #
    # # Other Settings
    # DEBUG: bool = Field(False)

    # Configuration for Pydantic
    class Config:
        env_file = ".env"  # Explicitly specify the .env file
        case_sensitive = False

    # @model_validator(mode="after")
    # def assemble_database_url(cls, values):
    #     """
    #     Constructs DATABASE_URL from individual components if not provided.
    #     """
    #     if not values.get("DATABASE_URL"):
    #         user = values.get("POSTGRES_USER", "postgres")
    #         password = values.get("POSTGRES_PASSWORD", "password")
    #         host = values.get("POSTGRES_HOST", "localhost")
    #         port = values.get("POSTGRES_PORT", 5432)
    #         db = values.get("POSTGRES_DB", "postgres")
    #
    #         values["DATABASE_URL"] = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    #
    #     return values

    # @model_validator(mode="after")
    # def assemble_redis_url(cls, values):
    #     """
    #     Constructs REDIS_URL from individual components if not provided.
    #     """
    #     if not values.get("REDIS_URL"):
    #         host = values.get("REDIS_HOST", "localhost")
    #         port = values.get("REDIS_PORT", 6379)
    #         db = values.get("REDIS_DB", 0)
    #         password = values.get("REDIS_PASSWORD")
    #
    #
    #         if password:
    #             values["REDIS_URL"] = f"redis://:{password}@{host}:{port}/{db}"
    #         else:
    #             values["REDIS_URL"] = f"redis://{host}:{port}/{db}"
    #
    #     return values


# Instantiate the settings
settings = Settings()
