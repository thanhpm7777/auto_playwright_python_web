from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BASE_URL: str = "https://hocvancungricky.com/"
    USER_EMAIL: str = "test1111@gmail.com"
    USER_PASSWORD: str = "123456"

    PW_HEADLESS: bool = True
    PW_BROWSER: str = "chromium"  # chromium | firefox | webkit
    PW_TIMEOUT: int = 10000

    STORAGE_STATE: str = "artifacts/storage_state.json"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
