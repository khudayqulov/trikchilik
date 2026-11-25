import pytest

from app.config import Settings


def test_settings_load_required_values(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("BOT_TOKEN", "test-token")
    monkeypatch.setenv("WEB_APP_URL", "https://shop.example")
    monkeypatch.setenv("PORT", "9000")

    settings = Settings.from_env()

    assert settings.bot_token == "test-token"
    assert settings.web_app_url == "https://shop.example"
    assert settings.port == 9000


@pytest.mark.parametrize("url", ["http://shop.example", "https://"])
def test_settings_reject_invalid_mini_app_urls(
    monkeypatch: pytest.MonkeyPatch,
    url: str,
) -> None:
    monkeypatch.setenv("BOT_TOKEN", "test-token")
    monkeypatch.setenv("WEB_APP_URL", url)

    with pytest.raises(RuntimeError, match="HTTPS URL"):
        Settings.from_env()

