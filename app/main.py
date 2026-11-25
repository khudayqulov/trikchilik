import asyncio

import uvicorn
from aiogram import Bot

from app.bot import run_bot
from app.config import Settings
from app.web import create_app


async def main() -> None:
    settings = Settings.from_env()
    bot = Bot(token=settings.bot_token)
    server = uvicorn.Server(
        uvicorn.Config(
            create_app(),
            host=settings.host,
            port=settings.port,
            log_level="info",
        )
    )

    try:
        await asyncio.gather(
            run_bot(bot, settings.web_app_url),
            server.serve(),
        )
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

