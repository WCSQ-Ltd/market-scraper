from decouple import config

DEFAULT_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

HEADERS = {
    'cookieToken': config('HEADERS_COOKIE_TOKEN', default=''),
    'session': config('HEADERS_SESSION', default=''),
    'userAgent': config('HEADERS_USER_AGENT', default=DEFAULT_USER_AGENT),
}

FORM_TOKEN = config('FORM_TOKEN', default='')
MARKET_URL = config('MARKET_URL', default='https://trade.sea.playblackdesert.com')
