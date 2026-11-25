# Tirikchilik Telegram bot

Telegram shop bot and a minimal Telegram Mini App. The initial version provides
the requested Uzbek menus and information text. The catalog is deliberately
empty, and checkout, basket persistence, feedback collection, contact details,
partnership details, and additional languages are not configured.

## Requirements

- Python 3.11+
- A Telegram bot token from BotFather
- A public HTTPS URL for the Mini App (Telegram requires HTTPS)

## Run locally

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -e ".[test]"
Copy-Item .env.example .env
```

Set `BOT_TOKEN` and `WEB_APP_URL` in `.env`, then load them into the process
environment and run the bot. For example, with PowerShell:

```powershell
py -m app.main
```

The web app is served at `/` and the health check at `/health` on the configured
host and port. The process also starts Telegram long polling. For local
development, expose the web server through an HTTPS tunnel and use that HTTPS
address as `WEB_APP_URL`.

## Render deployment

The repository includes `render.yaml` and a Docker-based build:

1. Create a Render account and connect this GitHub repository.
2. Choose **Blueprint** and select `render.yaml`.
3. Set `BOT_TOKEN` as a Render secret/environment variable.
4. Confirm that `WEB_APP_URL` matches the deployed Render URL.
5. In BotFather, configure the Mini App URL with the same HTTPS URL.

Do not place the bot token in `render.yaml`, Dockerfile, source code, or Git
commits. Render's generated HTTPS service URL is suitable for Telegram Mini
Apps.

## Tests

```powershell
py -m pytest
```
