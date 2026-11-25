import os
from dataclasses import dataclass
from urllib.parse import urlparse

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
    bot_token: str
    web_app_url: str
    host: str = "0.0.0.0"
    port: int = 8000

    @classmethod
    def from_env(cls) -> "Settings":
        load_dotenv()
        token = os.environ.get("BOT_TOKEN", "").strip()
        web_app_url = os.environ.get("WEB_APP_URL", "").strip()
        host = os.environ.get("HOST", "0.0.0.0").strip()

        if not token:
            raise RuntimeError("BOT_TOKEN must be set.")
        if not web_app_url:
            raise RuntimeError("WEB_APP_URL must be set.")
        parsed_web_app_url = urlparse(web_app_url)
        if parsed_web_app_url.scheme != "https" or not parsed_web_app_url.netloc:
            raise RuntimeError("WEB_APP_URL must be an HTTPS URL for Telegram Mini Apps.")

        try:
            port = int(os.environ.get("PORT", "8000"))
        except ValueError as exc:
            raise RuntimeError("PORT must be an integer.") from exc
        if not 1 <= port <= 65535:
            raise RuntimeError("PORT must be between 1 and 65535.")

        return cls(bot_token=token, web_app_url=web_app_url, host=host, port=port)

