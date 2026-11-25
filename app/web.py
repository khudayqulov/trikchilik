from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse

STATIC_DIR = Path(__file__).resolve().parent / "static"


def create_app() -> FastAPI:
    app = FastAPI(title="Tirikchilik Mini App")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}

    @app.get("/api/products")
    async def products() -> list[dict[str, str]]:
        return []

    @app.get("/")
    async def mini_app() -> FileResponse:
        return FileResponse(STATIC_DIR / "index.html")

    return app


app = create_app()

