from decouple import config

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

HEADERS = {
    'userAgent': config('HEADERS_USER_AGENT', default=DEFAULT_USER_AGENT),
}

MARKET_URL = config('MARKET_URL', default='https://trade.sea.playblackdesert.com')

SQLALCHEMY_DATABASE_URL = config('SQLALCHEMY_DATABASE_URL', default='sqlite:///scraper.db')

DISCORD_WEBHOOK_URL = config('DISCORD_WEBHOOK_URL', default='')

SCRAPE_SLEEP_SECONDS = config('SCRAPE_SLEEP_SECONDS', cast=int, default=60)
HEARTBEAT_RUN_COUNT_DIVISOR = config('HEARTBEAT_RUN_COUNT_DIVISOR', cast=int, default=60)
